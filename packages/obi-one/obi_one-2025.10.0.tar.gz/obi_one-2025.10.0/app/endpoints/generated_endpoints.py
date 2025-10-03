import re
import tempfile
from typing import Annotated, get_type_hints

import entitysdk.client
import entitysdk.common
from fastapi import APIRouter, Depends, HTTPException

from app.dependencies.entitysdk import get_client
from app.logger import L
from obi_one.core.form import Form
from obi_one.core.scan import GridScan
from obi_one.scientific.contribute.contribute import (
    ContributeMorphology,
    ContributeMorphologyForm,
    ContributeSubject,
    ContributeSubjectForm,
)
from obi_one.scientific.morphology_metrics.morphology_metrics import (
    MorphologyMetrics,
    MorphologyMetricsForm,
)
from obi_one.scientific.simulation.simulations import (
    Simulation,
    SimulationsForm,
)


def check_implementations_of_single_coordinate_class(
    single_coordinate_cls: type[Form], processing_method: str, data_postprocessing_method: str
) -> str | type | None:
    """Return the class of the return type of a processing_method of the single coordinate class.

    Returns None if return type not specified
    Returns message strings if the processing_method
    or data_postprocessing_method not implemented.
    """
    return_class = None

    # Check that the method is a method of the single coordinate class
    if not (
        hasattr(single_coordinate_cls, processing_method)
        and callable(getattr(single_coordinate_cls, processing_method))
    ):
        return f"{processing_method} is not a method of {single_coordinate_cls.__name__}"
    if not data_postprocessing_method:
        return None

    # Check that the data_postprocessing_method is a method of the single coordinate class
    if not (
        hasattr(single_coordinate_cls, data_postprocessing_method)
        and callable(getattr(single_coordinate_cls, data_postprocessing_method))
    ):
        return f"{data_postprocessing_method} is not a method of {single_coordinate_cls.__name__}"
    return_class = get_type_hints(getattr(single_coordinate_cls, data_postprocessing_method)).get(
        "return"
    )

    return return_class


def create_endpoint_for_form(
    model: type[Form],
    single_coordinate_cls: type[Form],
    router: APIRouter,
    processing_method: str,
    data_postprocessing_method: str,
) -> None:
    """Create a FastAPI endpoint for generating grid scans based on an OBI Form model."""
    # model_name: model in lowercase with underscores between words and "Forms" removed (i.e.
    # 'morphology_metrics_example')
    model_base_name = model.__name__.removesuffix("Form")
    model_name = "-".join([word.lower() for word in re.findall(r"[A-Z][^A-Z]*", model_base_name)])

    # Check which of single coordinate class, method, data_handling_method and return type
    # are implemented
    return_class = check_implementations_of_single_coordinate_class(
        single_coordinate_cls, processing_method, data_postprocessing_method
    )

    if not isinstance(return_class, str):
        # TODO: return_type = None if return_class is None else dict[str, return_class]
        #       => ERA001 Found commented-out code

        # Create endpoint name
        endpoint_name_with_slash = "/" + model_name + "-" + processing_method + "-grid"
        if data_postprocessing_method:
            endpoint_name_with_slash = endpoint_name_with_slash + "-" + data_postprocessing_method

        @router.post(endpoint_name_with_slash, summary=model.name, description=model.description)
        def endpoint(
            db_client: Annotated[entitysdk.client.Client, Depends(get_client)],
            form: model,
        ) -> str:
            L.info("generate_grid_scan")
            L.info(db_client)

            campaign = None
            try:
                with tempfile.TemporaryDirectory() as tdir:
                    grid_scan = GridScan(
                        form=form,
                        # TODO: output_root=settings.OUTPUT_DIR / "fastapi_test" / model_name
                        #        / "grid_scan", => ERA001 Found commented-out code
                        output_root=tdir,
                        coordinate_directory_option="ZERO_INDEX",
                    )
                    campaign = grid_scan.execute(
                        processing_method=processing_method,
                        data_postprocessing_method=data_postprocessing_method,
                        db_client=db_client,
                    )

            except Exception as e:
                error_msg = str(e)

                if len(e.args) == 1:
                    error_msg = str(e.args[0])
                elif len(e.args) > 1:
                    error_msg = str(e.args)

                L.error(error_msg)

                raise HTTPException(status_code=500, detail=error_msg) from e

            else:
                L.info("Grid scan generated successfully")
                if campaign is not None:
                    return str(campaign.id)

                L.info("No campaign generated")
                return ""


def activate_generated_endpoints(router: APIRouter) -> APIRouter:
    for form, processing_method, data_postprocessing_method, single_coordinate_cls in [
        (SimulationsForm, "generate", "", Simulation),
        (SimulationsForm, "generate", "save", Simulation),
        (MorphologyMetricsForm, "run", "", MorphologyMetrics),
        (ContributeMorphologyForm, "generate", "", ContributeMorphology),
        (ContributeSubjectForm, "generate", "", ContributeSubject),
    ]:
        create_endpoint_for_form(
            form,
            single_coordinate_cls,
            router,
            processing_method=processing_method,
            data_postprocessing_method=data_postprocessing_method,
        )
    return router

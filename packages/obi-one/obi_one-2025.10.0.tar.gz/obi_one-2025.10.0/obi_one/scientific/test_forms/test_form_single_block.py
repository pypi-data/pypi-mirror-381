import logging
from typing import ClassVar

from pydantic import Field

from obi_one.core.block import Block
from obi_one.core.form import Form
from obi_one.core.path import NamedPath
from obi_one.core.single import SingleCoordinateMixin
from obi_one.database.cell_morphology_from_id import CellMorphologyFromID

L = logging.getLogger("obi-one")


class SingleBlockGenerateTestForm(Form):
    """Test."""

    single_coord_class_name: ClassVar[str] = "SingleBlockGenerateTest"
    name: ClassVar[str] = "Single Block Generate Test"
    description: ClassVar[str] = "Test form for testing a single block form with entity SDK"

    class Initialize(Block):
        morphology_path: NamedPath | list[NamedPath]

    initialize: Initialize


class SingleBlockGenerateTest(SingleBlockGenerateTestForm, SingleCoordinateMixin):
    """Test."""

    @staticmethod
    def run() -> None:
        L.info("Running SingleBlockGenerateTest")


"""
Test Form for testing a single block form with entity SDK
"""


class SingleBlockEntityTestForm(Form):
    """Test Form for testing a single block form with entity SDK."""

    single_coord_class_name: ClassVar[str] = "SingleBlockGenerateTest"
    name: ClassVar[str] = "Single Block Entity Test"
    description: ClassVar[str] = "Test form for testing a single block form with entity SDK"

    class Initialize(Block):
        morphology: CellMorphologyFromID | list[CellMorphologyFromID]

    initialize: Initialize


class SingleBlockEntitySDKTest(SingleBlockEntityTestForm, SingleCoordinateMixin):
    """Test."""

    @staticmethod
    def run() -> None:
        L.info("Running SingleBlockEntitySDKTest")


class BlockForMultiBlockEntitySDKTest(Block):
    morphology_2: CellMorphologyFromID | list[CellMorphologyFromID]


class MultiBlockEntitySDKTestForm(Form):
    """Test."""

    single_coord_class_name: ClassVar[str] = "MultiBlockGenerateTest"
    name: ClassVar[str] = "Multi Block Entity Test"
    description: ClassVar[str] = "Test form for testing a single block form with entity SDK"

    test_blocks: dict[str, BlockForMultiBlockEntitySDKTest] = Field(description="Test blocks")

    class Initialize(Block):
        morphology: CellMorphologyFromID | list[CellMorphologyFromID]

    initialize: Initialize


class MultiBlockEntitySDKTest(MultiBlockEntitySDKTestForm, SingleCoordinateMixin):
    """Test."""

    @staticmethod
    def run() -> None:
        L.info("Running MultiBlockEntitySDKTest")

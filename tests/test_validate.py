
from tests.test_base import TestBase
from pathlib import Path
from src.validate import metadata_validator_factory
from src.classes.tool_metadata import ToolMetadata, ParentToolMetadata, SubtoolMetadata
from content_maps import tool_maps, script_maps, workflow_maps

class TestValidateMetadata(TestBase):

    def test_validate_tool_metadata(self):
        validate_tool_metadata = metadata_validator_factory(ToolMetadata)
        metadata_path = TestBase.get_metadata_path(tool_maps.gnu_tools['TL_e7d707.47'])
        validate_tool_metadata(metadata_path)
        return

    def test_validate_tool_metadata_fail(self):
        validate_tool_metadata = metadata_validator_factory(ToolMetadata)
        metadata_path = Path().cwd() / 'tests/test_files/bad_gawk-metadata.yaml'
        with self.assertRaises(ValueError):
            validate_tool_metadata(metadata_path)
        return

    def test_validate_parent_tool_metadata(self):
        validate_parent_metadata = metadata_validator_factory(ParentToolMetadata)
        metadata_path = Path(tool_maps.STAR['TL_8ab263.82'])
        validate_parent_metadata(metadata_path)

    def test_validate_parent_tool_metadata_fail(self):
        validate_parent_metadata = metadata_validator_factory(ParentToolMetadata)
        metadata_path = Path('tests/test_files/bad_samtools-metadata.yaml')
        with self.assertRaises(AttributeError):
            validate_parent_metadata(metadata_path)
        return

    def test_validate_subtool_metadata(self):
        validate_subtool_metadata = metadata_validator_factory(SubtoolMetadata)
        metadata_path = TestBase.get_metadata_path(tool_maps.STAR['TL_8ab263_a4.82'])  # alignReads
        validate_subtool_metadata(metadata_path)
        return

    def test_validate_subtool_metadata_fail(self):
        validate_subtool_metadata = metadata_validator_factory(SubtoolMetadata)
        metadata_path = Path('tests/test_files/bad_samtools-view-metadata.yaml')  # subtool name not in parent featurelist.
        with self.assertRaises(ValueError):
            validate_subtool_metadata(metadata_path)
        return




import configparser
import re
import tempfile
from pathlib import Path

test_rel_content_path = Path.cwd() / 'tests' / 'test_files' / 'test_content'
travis_root = Path('/home/travis/build/xDBio-Inc/cwl-source')
content_base_path = Path.cwd()

content_maps_dir_name = 'content_maps'

main_tool_subtool_name = '__main__'  # store here so can change easily. This is the 'name' of the main tool (categorized as a subtool).

instance_file_pattern = re.compile(r'[0-9a-f]{4}\.ya?ml')

instance_metadata_file_pattern = re.compile(r'[0-9a-f]{4}-metadata\.ya?ml')

script_common_metadata_file_pattern = re.compile(r'[A-Za-z_]+-metadata\.yaml')

common_dir_name = 'common'

instances_dir_name = 'instances'

root_repo_name = 'cwl-source'

tools_dir_name = 'cwl-tools'

scripts_dir_name = 'cwl-scripts'

workflows_dir_name = 'cwl-workflows'

def make_config_dict(base_path):
    base_path = Path(base_path)  # Make sure any string values are turned into Path objects.
    config_dict = {
        'base_path': base_path,
        'content_maps_dir': base_path / content_maps_dir_name,
        'temp_dir': tempfile.TemporaryDirectory(prefix='cwlTest_'),
    }
    return config_dict


# Default values for using tool in repos.
_default = make_config_dict(content_base_path)

# Test values for running unit tests.
_test = make_config_dict(test_rel_content_path)

_travis = make_config_dict(travis_root)

config = {'TEST': _test, 'DEFAULT': _default, 'TRAVIS': _travis}

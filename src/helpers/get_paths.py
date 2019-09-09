import os
from pathlib import Path
from src.config import config

# Misc

def get_inputs_schema_template():

    schema_template_path = Path.cwd() / 'tests/test_files/schema_salad/inputs_schema_template.yml'

    return schema_template_path

# cwl-tools

def get_tool_version_dir(tool_name, tool_version):
    version_dir = config[os.environ['CONFIG_KEY']]['cwl_tool_dir'] / tool_name / tool_version
    return version_dir


def get_cwl_tool(tool_name, tool_version, subtool_name=None):
    version_dir = get_tool_version_dir(tool_name, tool_version)

    if subtool_name:
        cwl_tool_path = version_dir / f"{tool_name}_{subtool_name}" / f"{tool_name}-{subtool_name}.cwl"
    else:
        cwl_tool_path = version_dir / f"{tool_name}" / f"{tool_name}.cwl"
    return cwl_tool_path


def get_cwl_tool_metadata(tool_name, tool_version, subtool_name=None, parent=False):
    version_dir = get_tool_version_dir(tool_name, tool_version)

    if parent:
        cwl_tool_metadata_path = version_dir / 'common' / f"{tool_name}-metadata.yaml"
    else:
        cwl_tool_metadata_path = get_metadata_path(get_cwl_tool(tool_name, tool_version, subtool_name=subtool_name))
    return cwl_tool_metadata_path

def get_tool_inputs(tool_name, tool_version, input_hash, subtool_name=None):

    cwl_tool_dir = get_cwl_tool(tool_name,tool_version, subtool_name=subtool_name).parent
    inputs_path = cwl_tool_dir / 'instances' / f"{input_hash}.yaml"

    return inputs_path

# cwl-scripts

def get_script_version_dir(group_name, project_name, version):
    script_ver_dir = config[os.environ['CONFIG_KEY']]['cwl_script_dir'] / group_name / project_name / version
    return script_ver_dir

def get_cwl_script(group_name, project_name, version, script_name):
    script_ver_dir = get_script_version_dir(group_name, project_name, version)
    script_path = script_ver_dir / script_name / f"{script_name}.cwl"
    return script_path

def get_script_metadata(group_name, project_name, version, script_name):
    script_ver_dir = get_script_version_dir(group_name, project_name, version)
    script_metadata_path = script_ver_dir / script_name / f"{script_name}-metadata.cwl"
    return script_metadata_path


def get_script_inputs():
    raise NotImplementedError


# cwl-workflows

def get_workflow_version_dir(group_name, project_name, version):
    workflow_ver_dir = config[os.environ['CONFIG_KEY']]['cwl_workflows_dir'] / group_name / project_name / version
    return workflow_ver_dir

def get_cwl_workflow(group_name, project_name, version, workflow_name):
    workflow_ver_dir = get_workflow_version_dir(group_name, project_name, version)
    workflow_path = workflow_ver_dir / f"{workflow_name}.cwl"
    return workflow_path

def get_workflow_metadata(group_name, project_name, version, workflow_name):
    workflow_ver_dir = get_workflow_version_dir(group_name, project_name, version)
    workflow_metadata_path = workflow_ver_dir / f"{workflow_name}-metadata.yaml"
    return workflow_metadata_path

def get_workflow_inputs():
    raise NotImplementedError



# helpers

def get_relative_path(full_path, base_path=Path.cwd()):

    return full_path.relative_to(base_path)

def get_metadata_path(cwl_path):
    if not isinstance(cwl_path, Path):
        cwl_path = Path(cwl_path)
    path_dir = cwl_path.parent
    metafile_name = f"{cwl_path.stem}-metadata.yaml"
    metadata_path = path_dir / metafile_name
    return metadata_path

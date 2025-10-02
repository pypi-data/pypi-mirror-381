from logging import getLogger
from logging.config import dictConfig as configure_logging
from pathlib import Path
from sys import exit

from click import Context, group, option, pass_context, pass_obj, version_option
from click import Path as ClickPath

from .. import (
    generate_base_workflow,
    generate_helper_script,
    generate_semantic_release_config,
)
from .. import (
    generate_reusable_workflow as generate_reusable_workflow,
)
from ..errors import CiStarterError
from ..logging_conf import logging_configuration
from ..utils import dump
from .callbacks import WorkDir as WorkDir
from .callbacks import set_module_name, set_workdir
from .validations import validate_test_group, validate_workflow_file_name

configure_logging(logging_configuration)

logger = getLogger(__name__)

entry_point_name = "ci-start"


@group(name=entry_point_name)
@version_option()
@option(
    "-C",
    "--project-path",
    "workdir",
    default=".",
    type=ClickPath(exists=True, dir_okay=True, writable=True, allow_dash=False, path_type=Path),
    callback=set_workdir,
)
@pass_context
def cli(
    context: Context,
    workdir: Path,
) -> None:
    context.obj = workdir


@cli.command()
@pass_obj
def psr_config(workdir):
    logger.debug("Psr-config got workdir %s", workdir)
    try:
        generate_semantic_release_config(workdir.project)
    except CiStarterError as err:
        logger.exception(err)
        exit(err.code)


@cli.command()
@option("-m", "--module_name")
@option(
    "--workflow-file-name",
    default="continuous-delivery.yml",
    type=ClickPath(writable=True, path_type=Path),
    callback=validate_workflow_file_name,
)
@option("--test-group", default="test", callback=validate_test_group)
@option("--test-command", default="uv run -- pytest --verbose")
@pass_obj
def workflows(
    workdir: WorkDir,
    module_name: str,
    workflow_file_name: Path,
    test_group: str,
    test_command: str,
):
    module_name = set_module_name(workdir.pyproject_toml, module_name)

    logger.debug("Workflows got workdir %s", workdir)
    logger.debug("module_name = %s", module_name)
    logger.debug("workflow_file_name = %s", workflow_file_name)
    logger.debug("workdir = %s", workdir)
    logger.debug("test_group = %s", test_group)
    logger.debug("test_command = %s", test_command)

    workdir.workflows.mkdir(parents=True, exist_ok=True)

    with workdir.helper_script.open("w", encoding="utf-8") as script_file:
        script: str = generate_helper_script()
        script_file.write(script)

    with workdir.base_workflow.open("w", encoding="utf-8") as base_workflow:
        data = generate_base_workflow()
        dump(data, base_workflow)

    for reusable_workflow_file_path in (workdir.build, workdir.release, workdir.test_e2e):
        with reusable_workflow_file_path.open("w", encoding="utf-8") as file:
            asset_path = Path(*reusable_workflow_file_path.parts[-2:])
            data = generate_reusable_workflow(asset_path)
            dump(data, file)

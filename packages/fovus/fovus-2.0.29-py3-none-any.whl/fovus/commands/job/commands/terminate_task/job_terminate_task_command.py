import click
from typing_extensions import Union

from fovus.adapter.fovus_api_adapter import FovusApiAdapter
from fovus.constants.cli_action_runner_constants import GENERIC_SUCCESS
from fovus.util.file_util import FileUtil
from fovus.util.util import Util


@click.command("terminate-task")
@click.argument("job_directory", type=Union[str, None], default=None, required=False)
@click.option(
    "--job-id",
    type=str,
    help=(
        "The ID of the job to terminate. This is only required if JOB_DIRECTORY has not been initialized by"
        " the Fovus CLI."
    ),
)
@click.option(
    "--run-id",
    type=str,
    help=("The task ID of the job to terminate."),
)
def job_terminate_task_command(
    job_id: Union[str, None],
    job_directory: Union[str, None],
    run_id: Union[str, None],
):
    """
    Terminate a running task in Fovus.

    This command will stop the task and release any resources associated with it.
    """
    print("Authenticating...")
    fovus_api_adapter = FovusApiAdapter()
    if not run_id:
        raise click.BadParameter(message="Missing run ID. This can be provided as an argument (via --run-id)")

    job_id = FileUtil.get_job_id(job_id, job_directory)
    print("Terminating task...")
    fovus_api_adapter.terminate_task(job_id, run_id)

    Util.print_success_message(GENERIC_SUCCESS)
    print(f"Task {run_id} from Job {job_id} has been terminated successfully.")

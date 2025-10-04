"""
Kamihi framework project execution.

License:
    MIT

"""

from typing import Annotated

import typer
from validators import ValidationError, hostname

from kamihi import KamihiSettings, _init_bot
from kamihi.base.config import LogLevel
from kamihi.cli.utils import import_actions, import_models

app = typer.Typer()


def host_callback(
    value: str | None,
) -> str | None:
    """
    Ensure the host value is valid.

    Args:
        value (str | None): The host value.

    Returns:
        str | None: The validated host value.

    """
    if value and isinstance(hostname(value, may_have_port=False), ValidationError):
        raise typer.BadParameter("Invalid host value")
    return value


@app.command()
def run(
    ctx: typer.Context,
    log_level: Annotated[
        LogLevel | None,
        typer.Option(
            "--log-level", "-l", help="Set the logging level for console loggers.", show_default=LogLevel.INFO
        ),
    ] = None,
    web_host: Annotated[
        str | None,
        typer.Option(
            ..., "--host", "-h", help="Host of the admin web panel", callback=host_callback, show_default="localhost"
        ),
    ] = None,
    web_port: Annotated[
        int | None,
        typer.Option(..., "--port", "-p", help="Port of the admin web panel", min=1024, max=65535, show_default="4242"),
    ] = None,
) -> None:
    """Run a project with the Kamihi framework."""
    settings = KamihiSettings.from_yaml(ctx.obj.config) if ctx.obj.config is not None else KamihiSettings()
    if web_host:
        settings.web.host = web_host
    if web_port:
        settings.web.port = web_port
    if log_level:
        settings.log.stdout_level = log_level
        settings.log.stderr_level = log_level
        settings.log.file_level = log_level
        settings.log.notification_level = log_level

    import_models(ctx.obj.cwd / "models")

    bot = _init_bot(settings)

    import_actions(ctx.obj.cwd / "actions")

    bot.start()

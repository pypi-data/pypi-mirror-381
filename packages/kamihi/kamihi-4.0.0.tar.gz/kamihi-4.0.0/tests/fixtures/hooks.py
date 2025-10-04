"""
Pytest hooks.

License:
    MIT

"""

import json

import pytest
from _pytest.nodes import Item
from _pytest.runner import CallInfo
from _pytest.terminal import TerminalReporter

from tests.fixtures.docker_container import KamihiContainer


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item: Item, call: CallInfo):
    # Let's ensure we are dealing with a test report
    if call.when == "call" and call.excinfo:
        # Get the fixture instance from the item
        kamihi_container: KamihiContainer = item.funcargs.get("kamihi_container")
        reporter: TerminalReporter = item.config.pluginmanager.get_plugin("terminalreporter")
        if kamihi_container:
            reporter.write_sep("=", f" Command logs for {item.name} ")
            for line in kamihi_container.command_logs:
                if line.startswith("$ "):
                    reporter.write_sep("-", line)
                elif line.startswith("Waiting for log:"):
                    reporter.write_sep(" ", line)
                    reporter.write_line("")
                else:
                    try:
                        reporter.write_line(kamihi_container.parse_log_json(line)["text"].strip())
                    except (json.JSONDecodeError, AssertionError):
                        reporter.write_line(line.strip())


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    report_data = getattr(config, "_docker_cleanup_report", None)
    if report_data:
        terminalreporter.write_sep("-", "Docker cleanup report")
        terminalreporter.write_line(
            f"{len(report_data['containers']['ContainersDeleted'] or [])} containers removed ({report_data['containers']['SpaceReclaimed'] / 1024 / 1024:.2f} MB)"
        )
        terminalreporter.write_line(
            f"{len(report_data['volumes']['VolumesDeleted'] or [])} volumes removed ({report_data['volumes']['SpaceReclaimed'] / 1024 / 1024:.2f} MB)"
        )
        terminalreporter.write_line(
            f"{len(report_data['images']['ImagesDeleted'] or [])} images removed ({report_data['images']['SpaceReclaimed'] / 1024 / 1024:.2f} MB)"
        )
        terminalreporter.write_line("\n")

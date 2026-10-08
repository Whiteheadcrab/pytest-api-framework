import logging
import os
import pytest

from utils.logger_utils import LoggerUtils


logger = logging.getLogger(__name__)


def pytest_addoption(parser):
    parser.addoption("--host", action="store", default="prod")
    parser.addoption("--isTrue", action="store", default="prod")


def update_environment(config):
    os.environ["PYTEST_ENV"] = config.getoption("--host").lower()


@pytest.hookimpl()
def pytest_configure(config):
    log_file = LoggerUtils.configure_logging()
    logger.info("Pytest log file created at %s", log_file)
    update_environment(config)


def pytest_runtest_logstart(nodeid, location):
    logger.info("Starting test: %s", nodeid)


def pytest_runtest_logreport(report):
    if report.when == "call":
        logger.info("Finished test: %s - %s", report.nodeid, report.outcome.upper())

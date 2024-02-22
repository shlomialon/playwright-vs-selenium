import os
import pytest
from datetime import datetime
from dynconfig import settings


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="qa")


@pytest.fixture(scope='session', autouse=True)
def config_loader(pytestconfig):
    settings.configure(FORCE_ENV_FOR_DYNACONF=pytestconfig.getoption("env"))


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    settings.configure(FORCE_ENV_FOR_DYNACONF=config.getoption("env"))
    report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),  settings.reports_path)
    config._metadata = None

    if not os.path.exists(report_path):
        os.makedirs(report_path)

    config.option.htmlpath = f'{report_path}report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.html'

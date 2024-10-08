
import allure
import pytest
from pathlib import Path
from appium import webdriver
from utilities import config_reader
from utilities.log_utils import logger
from allure_commons.types import AttachmentType
from appium.options.common.base import AppiumOptions
from appium.webdriver.appium_service import AppiumService, DEFAULT_PORT, DEFAULT_HOST

# log = logger(__name__, logging.INFO)

pytest_plugins = [
    "utilities.log_utils"
]


def pytest_addoption(parser):
    parser.addoption("--browser--")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function")
def appium_driver(request):
    global driver
    service_device = AppiumService()
    # service_device.start(args=['-p', '4723', '--base-path', '/', '--session-override'])

    parent_path = Path(__file__).resolve().parents[1]
    config_path = f'{parent_path}/configuration_data/devices_config.json'
    device_caps: dict[str, any] = config_reader.load_devices_config(config_path)

    device = device_caps['device_caps']['device2']
    url = 'http://127.0.0.1:4723'
    logger.info(f"appPackage :{device['appium:appPackage']}")
    logger.info(f"device_id  :{device['appium:deviceName']} ")
    driver = webdriver.Remote(command_executor=url, options=AppiumOptions().load_capabilities(device))

    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield driver
    driver.quit()
    service_device.stop()


@pytest.fixture
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_screenshot", attachment_type=AttachmentType.PNG)

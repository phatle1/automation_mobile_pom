import time
import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.common.base import AppiumOptions
from utilities import config_reader
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService, DEFAULT_PORT, DEFAULT_HOST
import os

# global driver

pytest_plugins = [
    "utilities.log_utils"
]


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


# adb shell
# dumpsys window displays | grep -E ‘mCurrentFocus’
# io.pizzahut.hutbot.qa/io.yum.MainActivity

@pytest.fixture(scope="function")
def appium_driver(request):
    service_device = AppiumService()
    service_device.start(args=['-p', '4723', '--base-path', '/', '--session-override'])
    time.sleep(2)

    device_caps: dict[str, any] = config_reader.load_devices_config("../configuration_data/devices_config.json")
    device = device_caps['device_caps']['device1']
    url = 'http://0.0.0.0:4723'
    driver = webdriver.Remote(command_executor=url, options=AppiumOptions().load_capabilities(device))

    request.cls.driver = driver
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
    service_device.stop()


@pytest.fixture
def log_on_failure(request, appium_driver):
    yield
    item = request.node
    driver = appium_driver
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

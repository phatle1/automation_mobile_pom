import os
import time
import allure
import pytest
import logging
from pathlib import Path
from appium import webdriver
from utilities import config_reader
from utilities.log_util import logger
from allure_commons.types import AttachmentType
from appium.options.common.base import AppiumOptions
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService, DEFAULT_PORT, DEFAULT_HOST

log = logger(__name__, logging.INFO)

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
    # service_device.start(args=['-p', '4723', '--base-path', '/', '--session-override'])
    parent_path = Path(__file__).resolve().parents[1]
    config_path = f'{parent_path}/configuration_data/devices_config.json'
    device_caps: dict[str, any] = config_reader.load_devices_config(config_path)
    device = device_caps['device_caps']['device1']
    url = 'http://0.0.0.0:4723'
    log.logger.info(f"url           :{url}")
    log.logger.info(f"parent_path   :{parent_path} ")
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

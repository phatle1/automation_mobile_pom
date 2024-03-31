from typing import Generator
import pytest
from appium.webdriver.appium_service import AppiumService


@pytest.mark.skip
def appium_service() -> Generator[AppiumService, None, None]:
    service = AppiumService()
    service.start(
        args=[
            '--address', '127.0.0.1', '-p', '4773', '--base-path', '/wd/hub'
        ]
    )
    try:
        yield service
    finally:
        service.stop()


@pytest.mark.skip('Unstable in CI env')
def test_appium_service(appium_service: AppiumService) -> None:
    assert appium_service.is_running
    assert appium_service.is_listening

import pytest
from utilities.log_utils import logger_decorator


@pytest.mark.flaky(reruns=1)
@pytest.mark.usefixtures("appium_driver", "log_on_failure")
class base_test:
    pass

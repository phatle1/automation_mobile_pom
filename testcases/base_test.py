import pytest

from utilities.data_access_object import data_access_object
from pages.login_screen import login_screen
from pages.vendor_tool_selector_screen import vendor_tool_selector_screen
from pages.manager_vendor_tool.store_selection_screen import store_selection_screen


@pytest.mark.flaky(reruns=1)
@pytest.mark.usefixtures("appium_driver", "log_on_failure")
class base_test:
    @pytest.fixture(scope="function")
    def log_in_out(self, username, password):
        login_home_screen = login_screen(self.driver)
        data_access = data_access_object
        vendor_tool = vendor_tool_selector_screen(self.driver)
        store_selection = store_selection_screen(self.driver)

        login_home_screen.func_login(user_name=username, pass_word=password)
        vendor_tool.action_tap_vendor_tool('manager')

        user_first_name = (data_access.get_user_information(username))
        store_selection.func_navigate_to_main_page(user_first_name['First Name'])
        yield
        print('log out')

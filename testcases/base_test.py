import pytest
from pages.login_screen import login_screen
from pages.manager_vendor_tool.best_voice_screen import best_voices_screen
from pages.vendor_tool_selector_screen import vendor_tool_selector_screen
from data_access_object_api.data_access_object_apis import data_access_object
from pages.manager_vendor_tool.store_selection_screen import store_selection_screen


@pytest.mark.flaky(reruns=1)
@pytest.mark.usefixtures("appium_driver", "log_on_failure")
class base_test:
    @pytest.fixture(scope="function")
    def log_in_out(self, username, password):
        login_home_screen = login_screen(self.driver)
        data_access = data_access_object
        user_details = data_access.get_user_information(username)
        data_access.update_user_information(username)
        vendor_tool = vendor_tool_selector_screen(self.driver)
        store_selection = store_selection_screen(self.driver)
        best_voices = best_voices_screen(self.driver)

        login_home_screen.func_login(user_name=username, pass_word=password)
        vendor_tool.action_tap_vendor_tool('manager')

        store_selection.func_navigate_to_main_page(user_details['First Name'])
        best_voices.func_close_best_voices_section()
        yield
        print('log out')

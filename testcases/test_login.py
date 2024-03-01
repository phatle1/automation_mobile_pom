import pytest
from testcases.base_test import base_test

from pages.login_screen import login_screen
from pages.vendor_tool_selector_screen import vendor_tool_selector_screen
from pages.manager_vendor_tool.store_selection_screen import store_selection_screen
from pages.manager_vendor_tool.routines_screen import routines_screen

from utilities import data_provider
from utilities import data_access_object


class Test_Login(base_test):

    # @pytest.fixture(scope="function")
    @pytest.mark.parametrize("username,password", data_provider.get_authentication("FBA"))
    def test_login_with_valid_authentication(self, username, password):
        home = login_screen(self.driver)
        data_access = data_access_object
        vendor_tool = vendor_tool_selector_screen(self.driver)
        store_selection = store_selection_screen(self.driver)

        home.func_login(user_name=username, pass_word=password)
        vendor_tool.action_tap_vendor_tool('manager')

        user_first_name = (data_access.data_access_object.get_user_information(username))
        store_selection.verify_user_logged_in_successfully(user_first_name['First Name'])

    def test_user_can_submit_a_routine(self):
        self.test_login_with_valid_authentication()
        routines = routines_screen(self.driver)



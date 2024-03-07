import pytest
from utilities import data_provider
from utilities import data_access_object
from testcases.base_test import base_test

from testcases.test_login import Test_Login
from pages.login_screen import login_screen
from pages.manager_vendor_tool.routines_screen import routines_screen
from pages.manager_vendor_tool.store_selection_screen import store_selection_screen


class Test_Routines(base_test):

    @pytest.mark.parametrize("username,password", data_provider.get_authentication("FBA"))
    def test_user_can_submit_a_routine(self, username, password, log_in_out):
        routines = routines_screen(self.driver)
        store_selection = store_selection_screen(self.driver)

        store_selection.func_navigate_to_main_page()
        routines.func_fill_all_checklist_items()





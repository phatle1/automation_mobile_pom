import pytest
from utilities import data_provider
from utilities import data_access_object
from testcases.base_test import base_test

from testcases.test_login import Test_Login
from pages.login_screen import login_screen
from pages.manager_vendor_tool.routines_screen import routines_screen
from pages.vendor_tool_selector_screen import vendor_tool_selector_screen
from pages.manager_vendor_tool.store_selection_screen import store_selection_screen



class Test_Routines(base_test):

    # @pytest.fixture(scope="function")

    def test_user_can_submit_a_routine(self):
        routines = routines_screen(self.driver)
        print("ajdhakjshd")
        print("ajdhajks")
        # Test_Login.test_login_with_valid_authentication()
        #
        # routines.action_fill_all_checklist_items()



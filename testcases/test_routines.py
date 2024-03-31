import pytest
from utilities import data_provider
from testcases.base_test import base_test
from utilities.data_access_object_apis import data_access_object
from pages.manager_vendor_tool.routines_screen import routines_screen
from pages.manager_vendor_tool.store_selection_screen import store_selection_screen


class Test_Routines(base_test):

    @pytest.mark.parametrize("username,password", data_provider.get_authentication("FBA"))
    @pytest.mark.regression
    def test_user_can_submit_a_routine(self, username, password, log_in_out):
        routines = routines_screen(self.driver)
        store_selection = store_selection_screen(self.driver)

        user_first_name = data_access_object.get_user_information(username)
        store_selection.func_navigate_to_main_page(user_first_name['First Name'])
        routines.func_fill_all_checklist_items()

    @pytest.mark.parametrize("username,password", data_provider.get_authentication("FBA"))
    @pytest.mark.smoke
    def test_user_cannot_submit_a_routine_if_any_completed_input(self, username, password, log_in_out):
        routines = routines_screen(self.driver)
        store_selection = store_selection_screen(self.driver)

        user_first_name = data_access_object.get_user_information(username)
        store_selection.func_navigate_to_main_page(user_first_name['First Name'])
        routines.func_fill_all_checklist_items()





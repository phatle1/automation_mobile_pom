import pytest
from utilities import data_provider
from testcases.base_test import base_test
from data_access_object_api.data_access_object_apis import data_access_object
from pages.manager_vendor_tool.activity_feed_screen import activity_feed_screen
from pages.manager_vendor_tool.store_selection_screen import store_selection_screen


class Test_Activity_Feed(base_test):

    @pytest.mark.parametrize("username,password", data_provider.get_authentication("FBA"))
    @pytest.mark.regression
    def test_user_can_submit_a_feed(self, username, password, log_in_out):
        store_selection = store_selection_screen(self.driver)
        activity_feed = activity_feed_screen(self.driver)

        user_details = data_access_object.get_user_information(username)
        store_selection.func_navigate_to_main_page(user_details['First Name'])
        activity_feed.action_tap_feed_bottom_bar_btn()
        activity_feed.action_tap_add_new_feed_btn()
        activity_feed.func_create_a_feed(is_image=True, is_attack=True, user_details=user_details)






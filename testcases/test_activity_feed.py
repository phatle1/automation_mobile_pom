import pytest
from utilities import data_provider
from utilities.data_access_object import data_access_object
from testcases.base_test import base_test

# from testcases.test_login import Test_Login
# from pages.login_screen import login_screen
from pages.manager_vendor_tool.routines_screen import routines_screen
from pages.manager_vendor_tool.store_selection_screen import store_selection_screen
from pages.manager_vendor_tool.activity_feed_screen import activity_feed_screen
from pages.manager_vendor_tool.activity_feed_create_post_screen import activity_feed_create_post_screen


class Test_Activity_Feed(base_test):

    @pytest.mark.parametrize("username,password", data_provider.get_authentication("FBA"))
    def test_user_can_submit_a_feed(self, username, password, log_in_out):
        store_selection = store_selection_screen(self.driver)
        activity_feed = activity_feed_screen(self.driver)
        activity_feed_create_post = activity_feed_create_post_screen(self.driver)

        user_first_name = data_access_object.get_user_information(username)
        store_selection.func_navigate_to_main_page(user_first_name['First Name'])
        activity_feed.action_tap_feed_bottom_bar_btn()
        activity_feed.action_tap_add_new_feed_btn()
        activity_feed_create_post.func_create_a_feed(is_image=True, is_attack=True, username=username)






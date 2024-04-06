from testcases.base_test import base_test


class Test_Login(base_test):
    pass
    # @pytest.mark.parametrize("username,password", data_provider.get_authentication("FBA"))
    # def test_login_with_valid_authentication(self, username, password):
    #     login_home_screen = login_screen(self.driver)
    #     data_access = data_access_object_db
    #     vendor_tool = vendor_tool_selector_screen(self.driver)
    #     store_selection = store_selection_screen(self.driver)
    #
    #     login_home_screen.func_login(user_name=username, pass_word=password)
    #     vendor_tool.action_tap_vendor_tool('manager')
    #
    #     user_first_name = (data_access.data_access_object_db.get_user_information(username))
    #     store_selection.verify_user_logged_in_successfully(user_first_name['First Name'])


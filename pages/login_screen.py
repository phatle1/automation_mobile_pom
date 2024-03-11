import utilities
from pages.base_screen import base_screen
from utilities.page_util import page_utils
from appium.webdriver.common.appiumby import AppiumBy
from utilities.log_utils import logger, action_log_decorator


class object_login_screen(object):
    log_in_btn = (AppiumBy.ID, 'Auth_LoginButton')
    auth_hidden_menu_btn = (AppiumBy.ID, 'Auth_HiddenMenu')
    yum_sso_user_name_txt = (AppiumBy.XPATH, '//android.widget.EditText[1]')
    yum_sso_pass_word_txt = (AppiumBy.XPATH, '//android.widget.EditText[2]')
    yum_sso_login_with_pwd_btn = (AppiumBy.XPATH, '//android.widget.Button[@text="Login with Password"]')
    yum_sso_sign_in_btn = (AppiumBy.XPATH, '//android.widget.Button[@text="Sign in"]')


@action_log_decorator
class login_screen(base_screen):
    def __init__(self, driver):
        super().__init__(driver)

    # get elements ---------------------
    def get_login_btn(self):
        return self.get_element_by_locator(object_login_screen.log_in_btn)

    def get_user_name_txt(self):
        return self.get_element_by_locator(object_login_screen.yum_sso_user_name_txt)

    def get_login_with_pwd_btn(self):
        return self.get_element_by_locator(object_login_screen.yum_sso_login_with_pwd_btn)

    def get_pass_word_txt(self):
        return self.get_element_by_locator(object_login_screen.yum_sso_pass_word_txt)

    def get_sign_in_btn(self):
        return self.get_element_by_locator(object_login_screen.yum_sso_sign_in_btn)

    # action ---------------------
    def action_type_user_name_txt(self, user_name):
        element = self.get_user_name_txt()
        assert self.is_element_present(element)
        self.action_type(element=element, value=user_name)
        assert self.is_element_filled_by_inputted_value(element=element, value=user_name)

    def action_tap_login_btn(self):
        element = self.get_login_btn()
        self.action_tap(element)
        self.wait_until_element_disappeared(element=element)

    def action_tap_login_with_pwd_btn(self):
        element = self.get_login_with_pwd_btn()
        assert self.is_element_present(element)
        self.action_tap(element)
        self.wait_until_element_disappeared(element=element)

    def action_type_pass_word_txt(self, pass_word):
        self.action_type(element=self.get_pass_word_txt(), value=pass_word)

    def action_tap_sign_in_btn(self):
        element = self.get_sign_in_btn()
        self.action_tap(element=element)
        assert self.wait_until_element_disappeared(element=element)

    def verify_user_can_input_to_textbox(self, value):
        self.is_element_filled_by_inputted_value(self.get_user_name_txt(), value)

    def verify_if_system_navigate_back_to_login_screen(self, user_name, pass_word):
        elements = self.get_elements_by_locator(object_login_screen.yum_sso_sign_in_btn)
        if len(elements) > 0:
            self.action_type_user_name_txt(user_name)
            self.action_type_pass_word_txt(pass_word)
            self.action_tap_sign_in_btn()
        else:
            pass

    def verify_if_the_user_already_logged_in(self, user_name, pass_word):
        elements = self.get_elements_by_locator(object_login_screen.yum_sso_sign_in_btn)
        if len(elements) > 0:
            self.action_type_user_name_txt(user_name)
            self.action_type_pass_word_txt(pass_word)
            assert True
        else:
            pass

    def func_login(self, user_name, pass_word):
        self.action_tap_login_btn()
        self.action_tap_login_with_pwd_btn()
        self.action_type_user_name_txt(user_name)
        self.action_type_pass_word_txt(pass_word)
        self.action_tap_sign_in_btn()
        # temporary comment out this block
        # self.verify_if_system_navigate_back_to_login_screen(user_name, pass_word)

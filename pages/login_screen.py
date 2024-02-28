from pages.base_screen import base_screen
from appium.webdriver.common.appiumby import AppiumBy


class object_login_screen(object):
    log_in_btn = (AppiumBy.ID, 'Auth_LoginButton')
    auth_hidden_menu_btn = (AppiumBy.ID, 'Auth_HiddenMenu')
    yum_sso_user_name_txt = (AppiumBy.ID, 'userId')
    yum_sso_login_with_pwd_btn = (AppiumBy.ID, 'loginwithpwdbtn')
    yum_sso_pass_word_txt = (AppiumBy.ID, 'password')
    yum_sso_sign_in_btn = (AppiumBy.ID, 'submit')

    # login_btn = "//android.view.ViewGroup[@resource-id='Auth_LoginButton']_XPATH"
    # hidden_menu_btn = "//android.view.ViewGroup[@resource-id='Auth_HiddenMenu']_XPATH"
    # user_name_txt = "//android.widget.EditText[@resource-id='userId']_XPATH"
    # login_with_pwd_btn = "//android.widget.Button[@resource-id='loginwithpwdbtn']_XPATH"
    # pass_word_txt = "//android.widget.EditText[@resource-id='password']_XPATH"
    # signin_btn = "//android.widget.Button[@resource-id='submit']_XPATH"


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
        self.action_type(element=element, value=user_name, element_name="Username text box")
        assert self.is_element_filled_by_inputted_value(element=element, value=user_name)

    def action_tap_login_btn(self):
        element = self.get_login_btn()
        self.action_tap(element, element_name="Login Button")
        self.wait_until_element_disappeared(element=element)

    def action_tap_login_with_pwd_btn(self):
        element = self.get_login_with_pwd_btn()
        assert self.is_element_present(element)
        self.action_tap(element, element_name="Login with Pass Word button")
        assert self.wait_until_element_disappeared(element=element)

    def action_type_pass_word_txt(self, pass_word):
        self.action_type(element=self.get_pass_word_txt(), value=pass_word, element_name="Pass Word text box")

    def action_tap_sign_in_btn(self):
        element = self.get_sign_in_btn()
        self.action_tap(element=element, element_name="Submit button")
        assert self.wait_until_element_disappeared(element=element)

    def verify_user_can_input_to_textbox(self, value):
        self.is_element_filled_by_inputted_value(self.get_user_name_txt(), value)

    def verify_if_system_navigate_back_to_login_screen(self, user_name, pass_word):
        if len(self.get_elements_by_locator(object_login_screen.yum_sso_sign_in_btn)) > 0:
            self.action_type_user_name_txt(user_name)
            self.action_type_pass_word_txt(pass_word)
            self.action_tap_sign_in_btn()
        else:
            pass

    def verify_if_the_user_already_logged_in(self, user_name, pass_word):
        if len(self.get_elements_by_locator(object_login_screen.yum_sso_sign_in_btn)) > 0:
            self.action_type_user_name_txt(user_name)
            self.action_type_pass_word_txt(pass_word)
            assert True
        else:
            pass

    def func_login(self, user_name, pass_word):
        self.action_tap_login_btn()
        self.action_type_user_name_txt(user_name)
        self.action_tap_login_with_pwd_btn()
        self.action_type_pass_word_txt(pass_word)
        self.action_tap_sign_in_btn()
        self.verify_if_system_navigate_back_to_login_screen(user_name, pass_word)

from pages.base_screen import base_screen


class object_login_screen(object):
    login_btn = "//android.view.ViewGroup[@resource-id='Auth_LoginButton']_XPATH"
    hidden_menu_btn = "//android.view.ViewGroup[@resource-id='Auth_HiddenMenu']_XPATH"
    user_name_txt = "//android.widget.EditText[@resource-id='userId']_XPATH"
    login_with_pwd_btn = "//android.widget.Button[@resource-id='loginwithpwdbtn']_XPATH"
    pass_word_txt = "//android.widget.EditText[@resource-id='password']_XPATH"
    signin_btn = "//android.widget.Button[@resource-id='submit']_XPATH"


class login_screen(base_screen):
    def __init__(self, driver):
        super().__init__(driver)

    # get elements ---------------------
    def login_btn(self):
        return self.get_element_by_locator(object_login_screen.login_btn)

    def user_name_txt(self):
        return self.get_element_by_locator(object_login_screen.user_name_txt)

    def login_with_pwd_btn(self):
        return self.get_element_by_locator(object_login_screen.login_with_pwd_btn)

    def pass_word_txt(self):
        return self.get_element_by_locator(object_login_screen.pass_word_txt)

    def submit_btn(self):
        return self.get_element_by_locator(object_login_screen.signin_btn)

    # action ---------------------
    def type_user_name_txt(self, user_name):
        element = self.user_name_txt()
        assert self.is_element_present(element)
        self.action_type(element=element, value=user_name, element_name="Username text box")
        assert self.is_element_filled_by_inputted_value(element=element, value=user_name)

    def tap_login_btn(self):
        element = self.login_btn()
        self.action_tap(element, element_name="Login Button")
        self.wait_until_element_disappeared(element=element)

    def tap_login_with_pwd_btn(self):
        element = self.login_with_pwd_btn()
        assert self.is_element_present(element)
        self.action_tap(element, element_name="Login with Pass Word button")
        assert self.wait_until_element_disappeared(element=element)

    def type_pass_word_txt(self, pass_word):
        self.action_type(element=self.pass_word_txt(), value=pass_word, element_name="Pass Word text box")

    def tap_sign_in_btn(self):
        element = self.submit_btn()
        self.action_tap(element=element, element_name="Submit button")
        assert self.wait_until_element_disappeared(element=element)

    def verify_user_can_input_to_textbox(self, value):
        self.is_element_filled_by_inputted_value(self.user_name_txt(), value)

    def verify_if_system_navigate_back_to_login_screen(self, user_name, pass_word):
        if len(self.get_elements_by_locator(object_login_screen.signin_btn)) > 0:
            self.type_user_name_txt(user_name)
            self.type_pass_word_txt(pass_word)
            self.tap_sign_in_btn()
        else:
            pass

    def login(self, user_name, pass_word):
        self.tap_login_btn()
        self.type_user_name_txt(user_name)
        self.tap_login_with_pwd_btn()
        self.type_pass_word_txt(pass_word)
        self.tap_sign_in_btn()
        self.verify_if_system_navigate_back_to_login_screen(user_name, pass_word)

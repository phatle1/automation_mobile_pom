from pages.base_screen import base_screen
from appium.webdriver.common.appiumby import AppiumBy

from utilities.log_utils import action_log_decorator


class objects_vendor_tool_selector_screen(object):
    manager_tool_btn = (AppiumBy.ID, 'VendorToolSelector_ShiftManagerAppButton')
    arl_tool_btn = (AppiumBy.ID, 'VendorToolSelector_AreaCoachAppButton')

    @staticmethod
    def welcome_lbl(user_first_name):
        return AppiumBy.XPATH, f"//android.widget.TextView[@text='Hi {user_first_name}!']"


@action_log_decorator
class vendor_tool_selector_screen(base_screen):
    def __init__(self, driver):
        super().__init__(driver)

    def get_manager_tool_btn(self):
        return self.get_element_by_locator(objects_vendor_tool_selector_screen.manager_tool_btn)

    def get_arl_tool_btn(self):
        return self.get_element_by_locator(objects_vendor_tool_selector_screen.arl_tool_btn)

    def get_welcome_lbl(self, user_first_name):
        return self.get_element_by_locator(objects_vendor_tool_selector_screen.welcome_lbl(user_first_name))

    # action -------------------------------

    def action_tap_manager_tool(self):
        self.action_tap(self.get_manager_tool_btn())

    def action_tap_arl_tool(self):
        self.action_tap(self.get_arl_tool_btn())

    def action_tap_vendor_tool(self, vendor_tool: str):
        self.action_tap_arl_tool() if vendor_tool.lower() == "arl" else self.action_tap_manager_tool()

    def verify_user_logged_in_successfully(self, user_first_name):
        assert self.is_element_present(self.get_welcome_lbl(user_first_name)) is True

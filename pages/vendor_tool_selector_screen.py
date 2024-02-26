from pages.base_screen import base_screen


class objects_vendor_tool_selector_screen(object):
    manager_tool_btn = "//android.view.ViewGroup[@resource-id='VendorToolSelector_ShiftManagerAppButton']_XPATH"
    arl_tool_btn = "//android.view.ViewGroup[@resource-id='VendorToolSelector_AreaCoachAppButton']_XPATH"

    @staticmethod
    def welcome_lbl(user_first_name):
        return f"//android.widget.TextView[@text='Hi {user_first_name}!']_XPATH"


class vendor_tool_selector_screen(base_screen):
    def __init__(self, driver):
        super().__init__(driver)

    def manager_tool_btn(self):
        return self.get_element_by_locator(objects_vendor_tool_selector_screen.manager_tool_btn)

    def arl_tool_btn(self):
        return self.get_element_by_locator(objects_vendor_tool_selector_screen.arl_tool_btn)

    def welcome_lbl(self, user_first_name):
        return self.get_element_by_locator(objects_vendor_tool_selector_screen.welcome_lbl(user_first_name))

    def tap_manager_tool(self):
        self.action_tap(self.manager_tool_btn(), element_name="Manager Vendor tool")

    def tap_arl_tool(self):
        self.action_tap(self.arl_tool_btn(), element_name="ARL Vendor tool")

    def tap_vendor_tool(self, vendor_tool: str):
        self.tap_arl_tool() if vendor_tool.lower() == "arl" else self.tap_manager_tool()

    def verify_user_logged_in_successfully(self, user_first_name):
        assert self.is_element_present(self.welcome_lbl(user_first_name)) is True

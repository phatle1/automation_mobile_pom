from pages.base_screen import base_screen


class objects_vendor_tool_selector_screen(object):
    manager_tool_btn = "VendorToolSelector_ShiftManagerAppButton_ID"
    arl_tool_btn = "VendorToolSelector_AreaCoachAppButton_ID"


class routines_screen(base_screen):
    def __init__(self, driver):
        super().__init__(driver)

    def manager_tool_btn(self):
        return self.get_element_by_locator(objects_vendor_tool_selector_screen.manager_tool_btn)

    def arl_tool_btn(self):
        return self.get_element_by_locator(objects_vendor_tool_selector_screen.arl_tool_btn)

    def tap_manager_tool(self):
        self.action_tap(self.manager_tool_btn())

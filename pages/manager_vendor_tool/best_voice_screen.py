from utilities import data_provider
from pages.base_screen import base_screen
from utilities.logic_utils import Logic_Util
from utilities.log_utils import action_log_decorator
from appium.webdriver.common.appiumby import AppiumBy


class objects_best_voices_screen(object):
    bv_title = (AppiumBy.XPATH, '//android.widget.TextView[@text="Where your voice matters!"]')
    bv_open_btn = (AppiumBy.XPATH, '//android.widget.TextView[@text="Open"]')
    bv_close_btn = (AppiumBy.XPATH, '//android.widget.TextView[@text="Close"]')
    bv_got_it_btn = (AppiumBy.XPATH, '//android.widget.TextView[@text="Got it!"]')


@action_log_decorator
class best_voices_screen(base_screen):
    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self):
        return self.get_element_by_locator(objects_best_voices_screen.bv_title)

    def get_bv_open_btn(self):
        return self.get_element_by_locator(objects_best_voices_screen.bv_open_btn)

    def get_bv_close_btn(self):
        return self.get_element_by_locator(objects_best_voices_screen.bv_close_btn)

    def get_bv_got_it_btn(self):
        return self.get_elements_by_locator(objects_best_voices_screen.bv_got_it_btn)

    # Action
    def action_tap_close(self):
        return self.action_tap(self.get_bv_close_btn())

    def action_tap_got_it_btn(self):
        return self.action_tap(self.get_bv_got_it_btn())

    # Assert
    def assert_best_voices_section_is_showing(self):
        self.assertTrue(self.is_element_present(self.get_title()))

    def assert_got_it_is_showing(self):
        self.assertTrue(self.is_element_present(self.get_bv_got_it_btn()))

    def assert_best_voices_section_is_disappeared(self):
        self.assertIsNone(self.get_bv_got_it_btn())

    # Func
    def func_close_best_voices_section(self):
        self.assert_best_voices_section_is_showing()
        self.action_tap_close()
        self.assert_got_it_is_showing()
        self.action_tap_got_it_btn()
        self.assert_best_voices_section_is_disappeared()

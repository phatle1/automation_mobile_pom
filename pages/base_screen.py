import logging
from utilities.log_util import logger
from utilities.page_util import page_utils
from selenium.webdriver.remote.webelement import WebElement
# from utilities.log_utils import logger, action_log_decorator


# log = logger(__name__, logging.INFO)

class base_screen:

    def __init__(self, driver):
        self.driver = driver
        self.page_utils = page_utils(self.driver)

    def get_elements(self, locator):
        self.page_utils.get_elements(locator)

    def get_element_by_type(self, method, value):
        self.page_utils.get_element_by_type(method, value)

    def get_element_by_locator(self, *locator):
        return self.page_utils.get_element_by_locator(*locator)

    def action_tap(self, element: WebElement):
        self.page_utils.action_tap(element)

    def action_tap_continuously(self, element: WebElement):
        self.page_utils.action_tap_continuously(element=element)

    def action_type(self, element: WebElement, value):
        self.page_utils.action_type(element=element, value=value)

    def click_index(self, locator, index):
        self.page_utils.click_index(locator, index)

    def get_text(self, locator):
        self.page_utils.get_text(locator)

    def is_visible(self, locator):
        self.page_utils.wait_until_element_to_be_visible(locator)

    def wait_visible(self, locator):
        self.page_utils.wait_visible(locator)

    def scroll_to_element(self, locator):
        self.page_utils.scroll_to_element(self, locator)

    def swipe_vertical(self, *locator):
        self.page_utils.swipe_vertical_to_element(*locator)

    def is_element_filled_by_inputted_value(self, element: WebElement, value):
        return self.page_utils.is_textbox_filled_by_value(element, value)

    def is_element_present(self, element: WebElement):
        return self.page_utils.is_element_present(element)

    def wait_until_element_to_be_visible(self, element: WebElement):
        return self.page_utils.wait_until_element_to_be_visible(element)

    def wait_until_element_disappeared(self, element: WebElement):
        return self.page_utils.wait_until_element_to_be_invisible(element)

    def get_elements_by_locator(self, *locator):
        return self.page_utils.get_elements_by_locator(*locator)

import logging
from time import sleep
from typing import List

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from multiprocessing import TimeoutError
from utilities.log_util import logger
from utilities import config_reader
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException, \
    StaleElementReferenceException

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By

log = logger(__name__, logging.INFO)


class page_utils(WebElement):
    def __init__(self, driver):
        self.driver = driver
        self.XPath = "_XPATH"
        self.ACCESSIBILITYID = "_ACCESSIBILITYID"
        self.CLASS_NAME = "_CLASS_NAME"
        self.ID = "_ID"
        self.user_action = ActionChains(driver)
        self.multi_action = MultiAction(driver)
        self.time_out: int = 30
        self.exceptions = [ElementNotVisibleException, NoSuchElementException, StaleElementReferenceException]
        # self.web_element = WebElement(driver)

    def get_elements(self, locator):
        method = locator[0]
        values = locator[1]

        if type(values) is str:
            return self.get_element_by_type(method, values)
        elif type(values) is list:
            for value in values:
                try:
                    return self.get_element_by_type(method, value)
                except NoSuchElementException:
                    pass
                raise NoSuchElementException

    def get_element_by_type(self, method, value):
        if method == 'accessibility_id':
            return self.driver.find_element_by_accessibility_id(value)
        elif method == 'android':
            return self.driver.find_element_by_android_uiautomator('new UiSelector().%s' % value)

    def get_element_by_locator(self, locator) -> WebElement:
        try:
            fluent_wait = WebDriverWait(self.driver, self.time_out, poll_frequency=5,
                                        ignored_exceptions=self.exceptions)
            log.logger.info(f"Element {str(locator)}")

            xpath_locator = config_reader.remove_locator_extension(locator, self.XPath)
            id_locator = config_reader.remove_locator_extension(locator, self.ID)
            accessibility_locator = config_reader.remove_locator_extension(locator, self.ACCESSIBILITYID)
            class_locator = config_reader.remove_locator_extension(locator, self.CLASS_NAME)

            if str(locator).endswith(self.XPath):
                return fluent_wait.until(expected_conditions.presence_of_element_located(
                    locator=(AppiumBy.XPATH, xpath_locator)))
            elif str(locator).endswith(self.ACCESSIBILITYID):
                return fluent_wait.until(expected_conditions.presence_of_element_located(
                    locator=(AppiumBy.ACCESSIBILITY_ID, accessibility_locator)))
            elif str(locator).endswith(self.ID):
                return fluent_wait.until(expected_conditions.presence_of_element_located(
                    locator=(AppiumBy.ID, id_locator)))
            elif str(locator).endswith(self.CLASS_NAME):
                return fluent_wait.until(expected_conditions.presence_of_element_located(
                    locator=(AppiumBy.CLASS_NAME, class_locator)))

            log.logger.info(f"Element {str(locator)}")
        except NoSuchElementException:
            log.logger.error(f"{str(NoSuchElementException)}  " + str(locator))
            pass
        except StaleElementReferenceException:
            log.logger.error(f"{str(StaleElementReferenceException)}  " + str(locator))
            pass
        except ElementNotVisibleException:
            log.logger.error(f"{str(ElementNotVisibleException)}  " + str(locator))
            pass

    def get_elements_by_locator(self, locator) -> list[WebElement]:
        try:
            if str(locator).endswith(self.XPath):
                xpath_locator = config_reader.remove_locator_extension(locator, self.XPath)
                return self.driver.find_elements(by=AppiumBy.XPATH, value=xpath_locator)
            elif str(locator).endswith(self.ACCESSIBILITYID):
                accessibility_locator = config_reader.remove_locator_extension(locator, self.ACCESSIBILITYID)
                return self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID(accessibility_locator))
            elif str(locator).endswith(self.ID):
                id_locator = config_reader.remove_locator_extension(locator, self.ID)
                return self.driver.ind_elements(AppiumBy.ID(id_locator))
            elif str(locator).endswith(self.CLASS_NAME):
                class_locator = config_reader.remove_locator_extension(locator, self.CLASS_NAME)
                return self.driver.find_elements(AppiumBy.CLASS_NAME(class_locator))
            log.logger.info(f"Element {str(locator)}")
        except NoSuchElementException:
            log.logger.error(f"{str(NoSuchElementException)}  " + str(locator))
            pass
        except StaleElementReferenceException:
            log.logger.error(f"{str(StaleElementReferenceException)}  " + str(locator))
            pass
        except ElementNotVisibleException:
            log.logger.error(f"{str(ElementNotVisibleException)}  " + str(locator))
            pass

    def action_tap(self, element: WebElement) -> None:
        try:
            self.wait_until_element_to_be_visible(element)
            self.wait_until_element_to_be_clickable(element)
            self.user_action.click(on_element=element).perform()
        except self.exceptions:
            log.logger.error(f"Element not found: {str(element)}")

    def action_tap_continuously(self, element: WebElement) -> None:
        try:
            i = 0
            while expected_conditions.element_to_be_clickable(element):
                try:
                    self.user_action.click(on_element=element).perform()
                except self.exceptions:
                    sleep(1)
                    i += 3
            raise Exception('Element never became visible: %s (%s)' % (element[0], element[0]))
        except self.exceptions:
            log.logger.error(f"Element not found: {str(element)}")

    def action_type(self, element: WebElement, value) -> None:
        try:
            self.wait_until_element_to_be_clickable(element)
            self.user_action.click(on_element=element).perform()
            self.user_action.send_keys(value).perform()
        except NoSuchElementException:
            log.logger.error(f"Element not found: {str(element)}")

    def action_type_enter(self, element: WebElement):
        try:
            self.wait_until_element_to_be_clickable(element)
            self.user_action.send_keys_to_element(element, Keys.ENTER).perform()
        except NoSuchElementException:
            log.logger.error(f"Element not found: {str(element)}")

    def drag_and_drop(self, from_element: WebElement, to_element: WebElement):
        try:
            self.user_action.drag_and_drop(from_element, to_element).perform()
        except NoSuchElementException:
            log.logger.error(f"Elements not found: {str(from_element)} and {str(to_element)}")

    def click_index(self, locator, index):
        try:
            if str(locator).endswith("_XPATH"):
                self.driver.find_elements_by_xpath(config_reader.read_config("locators: ", locator))[index].click()
            elif str(locator).endswith("_ACCESSIBILITYID"):
                self.driver.find_elements_by_accessibility_id(config_reader.read_config("locators: ", locator))[
                    index].click()
            elif str(locator).endswith("_ID"):
                self.driver.find_elements_by_id(config_reader.read_config("locators: ", locator))[index].click()
            log.logger.info("Clicking on an Element: " + str(locator) + "with index: " + str(index))
        except NoSuchElementException:
            log.logger.error("Element not found: " + str(locator))

    def get_text(self, element: WebElement):
        try:
            text = element.text
            log.logger.info(f"Getting text from an element: {text}")
            return text
        except self.exceptions:
            log.logger.error(f"Element not found: {str(element)}")

    def wait_until_element_to_be_visible(self, element: WebElement) -> WebElement | bool:
        try:
            fluent_wait = WebDriverWait(self.driver, self.time_out, poll_frequency=5,
                                        ignored_exceptions=self.exceptions)
            return fluent_wait.until(expected_conditions.visibility_of(element=element))
        except NoSuchElementException:
            pass
        except StaleElementReferenceException:
            pass
        except ElementNotVisibleException:
            pass
        except TimeoutException:
            pass

    def wait_until_element_to_be_clickable(self, element: WebElement):
        try:
            fluent_wait = WebDriverWait(self.driver, self.time_out, poll_frequency=5,
                                        ignored_exceptions=self.exceptions)
            fluent_wait.until(expected_conditions.element_to_be_clickable(element))
        except NoSuchElementException:
            pass
        except StaleElementReferenceException:
            pass
        except ElementNotVisibleException:
            pass
        except TimeoutException:
            pass

    def wait_until_element_to_be_invisible(self, element: WebElement):
        try:
            fluent_wait = WebDriverWait(self.driver, self.time_out, poll_frequency=5,
                                        ignored_exceptions=self.exceptions)
            return fluent_wait.until(expected_conditions.invisibility_of_element(element))
        except NoSuchElementException:
            pass
        except StaleElementReferenceException:
            pass
        except ElementNotVisibleException:
            pass
        except TimeoutException:
            pass

    def wait_until_element_to_be_selected(self, element: WebElement):
        try:
            fluent_wait = WebDriverWait(self.driver, self.time_out, poll_frequency=5,
                                        ignored_exceptions=self.exceptions)
            fluent_wait.until(expected_conditions.element_to_be_selected(element))
        except NoSuchElementException:
            pass
        except StaleElementReferenceException:
            pass
        except ElementNotVisibleException:
            pass
        except TimeoutException:
            pass

    def wait_visible(self, element: WebElement):
        try:
            i = 0
            while i != self.time_out:
                try:
                    self.wait_until_element_to_be_visible(element)
                    return self.get_element_by_locator(element)
                except NoSuchElementException:
                    sleep(1)
                    i += 1
            raise Exception('Element never became visible: %s (%s)' % (element[0], element[0]))
        except NoSuchElementException:
            pass
        except StaleElementReferenceException:
            pass
        except ElementNotVisibleException:
            pass
        except TimeoutException:
            pass

    @staticmethod
    def swipe_horizontal(direction, locator, times):
        try:
            if str(direction).lower() == 'right':
                pass
            elif str(direction).lower() == 'left':
                pass
        except NoSuchElementException:
            pass
        except StaleElementReferenceException:
            pass
        except ElementNotVisibleException:
            pass
        except TimeoutException:
            pass

    def scroll_to_element(self, locator):
        element = self.get_elements(locator)
        try:
            element

        except NoSuchElementException:
            pass
        except StaleElementReferenceException:
            pass
        except ElementNotVisibleException:
            pass
        except TimeoutException:
            pass

    def long_press(self):
        pass

    def pinch(self):
        try:
            xx = self.driver.get_window_size()['width'] / 2
            yy = self.driver.get_window_size()['height'] / 2
            action1 = TouchAction(self.driver)
            action2 = TouchAction(self.driver)
            zoom_action = MultiAction(self.driver)
            action1.long_press(x=xx, y=yy).move_to(x=0, y=50).wait(500).release()
            action2.long_press(x=xx, y=yy).move_to(x=0, y=-50).wait(500).release()
            zoom_action.add(action1, action2)
        except NoSuchElementException:
            pass
        except StaleElementReferenceException:
            pass
        except ElementNotVisibleException:
            pass
        except TimeoutException:
            pass

    @staticmethod
    def verify_equal(expected, actual):
        try:
            return True if (expected == actual) else False, f"{expected} is not equal {actual}"

        except NoSuchElementException:
            pass
        except StaleElementReferenceException:
            pass
        except ElementNotVisibleException:
            pass
        except TimeoutException:
            pass

    def is_element_present(self, element: WebElement):
        try:
            return True if self.wait_until_element_to_be_visible(
                element) is True else False, f"Element {element.__name__} is not visible"

        except NoSuchElementException:
            pass
        except StaleElementReferenceException:
            pass
        except ElementNotVisibleException:
            pass
        except TimeoutException:
            pass

    def is_textbox_filled_by_value(self, element: WebElement, value):
        try:
            self.wait_until_element_to_be_visible(element=element)
            return True if element.text == value else False, f"{element.text} is not equal {value}"
        except NoSuchElementException:
            pass
        except StaleElementReferenceException:
            pass
        except ElementNotVisibleException:
            pass
        except TimeoutException:
            pass

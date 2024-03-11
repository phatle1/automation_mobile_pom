import logging
import time
from time import sleep
from typing import List, Any

from utilities import config_reader
from selenium.webdriver import Keys
from utilities.log_utils import logger
from multiprocessing import TimeoutError
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.webelement import WebElement
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException, \
    StaleElementReferenceException

# For W3C actions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder


# log = logger(__name__, logging.INFO)


class page_utils(WebElement):
    def __init__(self, driver):
        self.driver = driver
        self.XPath = "_XPATH"
        self.ACCESSIBILITYID = "_ACCESSIBILITYID"
        self.CLASS_NAME = "_CLASS_NAME"
        self.ID = "_ID"
        self.user_action = ActionChains(driver)
        self.time_out: int = 40
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

    def get_element_by_locator(self, *locator) -> WebElement:
        try:
            locator = (locator[0][0], locator[0][1])
            fluent_wait = WebDriverWait(self.driver, self.time_out, poll_frequency=3,
                                        ignored_exceptions=self.exceptions)
            return fluent_wait.until(expected_conditions.presence_of_element_located(locator=locator))

        except NoSuchElementException:
            pass
        except ElementNotVisibleException:
            pass
        except StaleElementReferenceException:
            pass

    def get_elements_by_locator(self, *locator) -> Any | None:
        try:
            i = 0
            while i < self.time_out:
                element = self.driver.find_elements(locator[0][0], locator[0][1])
                if element is not None:
                    return element

                time.sleep(1)
                i += 3
                return element
        except Exception as ex:
            raise ex

    def action_tap(self, element: WebElement) -> None:
        try:
            self.wait_until_element_to_be_visible(element)
            self.wait_until_element_to_be_clickable(element)
            self.user_action.click(on_element=element).perform()
        except Exception as ex:
            raise ex

    def action_tap_continuously(self, element: WebElement) -> None:
        try:
            i = 0
            while expected_conditions.element_to_be_clickable(element):
                try:
                    self.user_action.click(on_element=element).perform()
                except self.exceptions:
                    sleep(1)
                    i += 3

            raise Exception('Element never became visible:')
        except Exception as ex:
            raise ex

    def action_type(self, element: WebElement, value) -> None:
        try:
            self.wait_until_element_to_be_clickable(element)
            self.user_action.click(on_element=element).perform()
            self.user_action.send_keys(value).perform()
        except Exception as ex:
            raise ex

    def action_type_enter(self, element: WebElement):
        try:
            self.wait_until_element_to_be_clickable(element)
            self.user_action.send_keys_to_element(element, Keys.ENTER).perform()
        except Exception as ex:
            raise ex

    def drag_and_drop(self, from_element: WebElement, to_element: WebElement):
        try:
            self.user_action.drag_and_drop(from_element, to_element).perform()
        except Exception as ex:
            raise ex

    def click_index(self, locator, index):
        try:
            if str(locator).endswith("_XPATH"):
                self.driver.find_elements_by_xpath(config_reader.read_config("locators: ", locator))[index].click()
            elif str(locator).endswith("_ACCESSIBILITYID"):
                self.driver.find_elements_by_accessibility_id(config_reader.read_config("locators: ", locator))[
                    index].click()
            elif str(locator).endswith("_ID"):
                self.driver.find_elements_by_id(config_reader.read_config("locators: ", locator))[index].click()
            logger.info("Clicking on an Element: " + str(locator) + "with index: " + str(index))
        except NoSuchElementException:
            logger.error("Element not found: " + str(locator))

    def get_text(self, element: WebElement):
        try:
            text = ''
            if element.text is not None:
                text = element.text
            else:
                text = ''
            logger.info(f"Getting text from element: {text}")
            return text
        except self.exceptions:
            logger.error(f"Element not found: {str(element)}")

    def wait_until_element_to_be_visible(self, element: WebElement) -> WebElement | bool:
        try:
            fluent_wait = WebDriverWait(self.driver, self.time_out, poll_frequency=5,
                                        ignored_exceptions=self.exceptions)
            return fluent_wait.until(expected_conditions.visibility_of(element=element))
        except NoSuchElementException:
            raise NoSuchElementException
        except StaleElementReferenceException:
            raise StaleElementReferenceException
        except ElementNotVisibleException:
            raise ElementNotVisibleException
        except TimeoutException:
            raise TimeoutException

    def wait_until_element_to_be_clickable(self, element: WebElement):
        try:
            fluent_wait = WebDriverWait(self.driver, self.time_out, poll_frequency=5,
                                        ignored_exceptions=self.exceptions)
            return fluent_wait.until(expected_conditions.element_to_be_clickable(element))
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
            raise Exception(f'Element never became visible: ')
        except NoSuchElementException:
            pass
        except StaleElementReferenceException:
            pass
        except ElementNotVisibleException:
            pass
        except TimeoutException:
            pass

    def swipe_vertical_to_element(self, *locator):
        try:
            window_size = self.driver.get_window_size()
            width = window_size["width"]
            height = window_size["height"]
            start_x = width / 2
            start_y = height / 2
            end_x = start_x
            end_y = start_y - 300
            is_swipe = True
            while is_swipe:
                try:
                    self.user_action.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
                    self.user_action.w3c_actions.pointer_action.move_to_location(x=start_x, y=start_y)
                    self.user_action.w3c_actions.pointer_action.pointer_down()
                    self.user_action.w3c_actions.pointer_action.move_to_location(x=end_x, y=end_y)
                    self.user_action.w3c_actions.pointer_action.release()
                    self.user_action.perform()
                    element = self.get_elements_by_locator(*locator)
                    if len(element) > 0:
                        is_swipe = False
                except NoSuchElementException:
                    pass
        except NoSuchElementException:
            pass
        except StaleElementReferenceException:
            pass
        except ElementNotVisibleException:
            pass
        except TimeoutException:
            pass

    @staticmethod
    def is_element_present(element: WebElement):
        try:
            return element.is_displayed()
            # """
            # return True if self.wait_until_element_to_be_visible(
            #     element) is True else False, f"Element {element.__name__} is not visible"
            # """

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

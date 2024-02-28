from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import unittest
import logging

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By

options = UiAutomator2Options()
options.load_capabilities({
    "platformName": "Android",
    "appium:deviceName": "emulator-5554",
    "appium:automationName": "UiAutomator2",
    "appium:app": "/Users/lephat/Downloads/signed.apk",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True,
    "appium:disableIdLocatorAutocompletion": True


})



def test_simple():
    driver = webdriver.Remote("http://0.0.0.0:4723", options=options)
    # driver.find_elements()
    driver.implicitly_wait(30)

    el1 = driver.find_element(by=AppiumBy.ID, value="Auth_LoginButton")


    # el1 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='Auth_LoginButton']")
    el1.click()
    # action_chain = ActionChains(driver)
    # # logger.info('hello this is Phat')
    # action_chain.click(el1[0]).perform()
    # print("đay ne ---------------------")
    # el1[0].click()
    driver.implicitly_wait(10)
    el2 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
    el2.send_keys("gcv2701")
    driver.implicitly_wait(10)
    el3 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@resource-id='loginwithpwdbtn']")
    el3.click()

    assertion = unittest.TestCase()
    assertion.assertEqual(1, 1, 'Not equal')
    driver.quit()

from pages.base_screen import base_screen
from appium.webdriver.common.appiumby import AppiumBy


class objects_store_selection_screen(object):
    # basic store selection
    search_bar_txt = (AppiumBy.ID, 'SearchBar_TextInput')
    choose_your_restaurant_txt = (AppiumBy.XPATH, "(//android.widget.TextView)[2]")
    logout_btn = (AppiumBy.XPATH, "(//android.widget.TextView//ancestor::android.view.ViewGroup//com.horcrux.svg.SvgView)[1]")
    kfc_ico = (AppiumBy.XPATH, "//*[@resource-id='SearchBar_TextInput']/parent::android.view.ViewGroup/android.view.ViewGroup[2]_XPATH")
    pizza_hut_ico = (AppiumBy.XPATH, "//*[@resource-id='SearchBar_TextInput']/parent::android.view.ViewGroup/android.view.ViewGroup[1]")
    map_switcher_btn = (AppiumBy.XPATH, "(//android.widget.TextView//ancestor::android.view.ViewGroup//com.horcrux.svg.SvgView)[2]")

    # store selection with map
    map_area = (AppiumBy.XPATH, "(//android.widget.RelativeLayout)[2]")
    zoom_in_btn = (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Zoom in']")
    zoom_out_btn = (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Zoom out']")
    my_location_btn = (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='My Location']")
    first_store_selection = (AppiumBy.XPATH, "//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[1]")

    # confirmation screen
    yes_btn = (AppiumBy.ID, "Store_Yes")

    @staticmethod
    def welcome_lbl(user_first_name):
        return AppiumBy.XPATH, f"//android.widget.TextView[@text='Hi {user_first_name}!']"

    @staticmethod
    def store_selection_lbl(internal_store_number):
        return AppiumBy.XPATH, f"//*[@resource-id='SearchBar_TextInput']/parent::android.view.ViewGroup//android.widget.ScrollView//*[@resource-id='StoreListItemNative_{internal_store_number}']"


class store_selection_screen(base_screen):
    def __init__(self, driver):
        super().__init__(driver)

    # Get elements section
    def get_search_bar_txt(self):
        return self.get_element_by_locator(objects_store_selection_screen.search_bar_txt)

    def get_pizza_hut_ico(self):
        return self.get_element_by_locator(objects_store_selection_screen.pizza_hut_ico)

    def get_kfc_ico(self):
        return self.get_element_by_locator(objects_store_selection_screen.kfc_ico)

    def get_my_location_btn(self):
        return self.get_element_by_locator(objects_store_selection_screen.my_location_btn)

    def get_first_store_selection(self):
        return self.get_element_by_locator(objects_store_selection_screen.first_store_selection)

    def get_zoom_in_btn(self):
        return self.get_element_by_locator(objects_store_selection_screen.zoom_in_btn)

    def get_zoom_out_btn(self):
        return self.get_element_by_locator(objects_store_selection_screen.zoom_out_btn)

    def get_welcome_lbl(self, user_first_name):
        return self.get_element_by_locator(objects_store_selection_screen.welcome_lbl(user_first_name))

    def get_choose_your_restaurant_txt(self):
        return self.get_element_by_locator(objects_store_selection_screen.choose_your_restaurant_txt)

    def get_yes_btn(self):
        return self.get_element_by_locator(objects_store_selection_screen.yes_btn)

    # Verify section
    def verify_user_log_in_successful(self):
        assert self.is_element_present(self.get_choose_your_restaurant_txt())

    def verify_user_logged_in_successfully(self, user_first_name):
        assert self.is_element_present(self.get_welcome_lbl(user_first_name)) is True, 'The expected result is not matches with actual'

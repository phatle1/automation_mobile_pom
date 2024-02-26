from pages.base_screen import base_screen


class objects_store_selection_screen(object):
    # basic store selection
    search_bar_txt = "//android.widget.EditText[@resource-id='SearchBar_TextInput']_XPATH"
    pizza_hut_ico = "//*[@resource-id='SearchBar_TextInput']/parent::android.view.ViewGroup/android.view.ViewGroup[1]_XPATH"
    kfc_ico = "//*[@resource-id='SearchBar_TextInput']/parent::android.view.ViewGroup/android.view.ViewGroup[2]_XPATH"
    map_switcher_btn = "(//android.widget.TextView//ancestor::android.view.ViewGroup//com.horcrux.svg.SvgView)[2]"
    logout_btn = "(//android.widget.TextView//ancestor::android.view.ViewGroup//com.horcrux.svg.SvgView)[1]"
    choose_your_restaurant_txt = "(//android.widget.TextView)[2]"

    # store selection with map
    my_location_btn = "//android.widget.ImageView[@content-desc='My Location']"
    map_area = "(//android.widget.RelativeLayout)[2]"
    first_store_selection = "//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[1]"
    zoom_in_btn = "//android.widget.ImageView[@content-desc='Zoom in']"
    zoom_out_btn = "//android.widget.ImageView[@content-desc='Zoom out']"

    @staticmethod
    def welcome_lbl(user_first_name):
        return f"//android.widget.TextView[@text='Hi {user_first_name}!']_XPATH"

    @staticmethod
    def store_selection_lbl(internal_store_number):
        return f"//*[@resource-id='SearchBar_TextInput']/parent::android.view.ViewGroup//android.widget.ScrollView//*[@resource-id='StoreListItemNative_{internal_store_number}']_XPATH"


class store_selection_screen(base_screen):
    def __init__(self, driver):
        super().__init__(driver)

    # Get elements section
    def search_bar_txt(self):
        return self.get_element_by_locator(objects_store_selection_screen.search_bar_txt)

    def pizza_hut_ico(self):
        return self.get_element_by_locator(objects_store_selection_screen.pizza_hut_ico)

    def kfc_ico(self):
        return self.get_element_by_locator(objects_store_selection_screen.kfc_ico)

    def my_location_btn(self):
        return self.get_element_by_locator(objects_store_selection_screen.my_location_btn)

    def first_store_selection(self):
        return self.get_element_by_locator(objects_store_selection_screen.first_store_selection)

    def zoom_in_btn(self):
        return self.get_element_by_locator(objects_store_selection_screen.zoom_in_btn)

    def zoom_out_btn(self):
        return self.get_element_by_locator(objects_store_selection_screen.zoom_out_btn)

    def welcome_lbl(self, user_first_name):
        return self.get_element_by_locator(objects_store_selection_screen.welcome_lbl(user_first_name))

    def choose_your_restaurant_txt(self):
        return self.get_element_by_locator(objects_store_selection_screen.choose_your_restaurant_txt)

    # Verify section
    def verify_user_log_in_successful(self):
        assert self.is_element_present(self.choose_your_restaurant_txt())

    def verify_user_logged_in_successfully(self, user_first_name):
        assert self.is_element_present(self.welcome_lbl(user_first_name)) is True

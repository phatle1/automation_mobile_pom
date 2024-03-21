from pages.base_screen import base_screen
from appium.webdriver.common.appiumby import AppiumBy


class objects_activity_feed_create_post_screen(object):
    create_post_lbl = (AppiumBy.XPATH, '//android.widget.TextView[@text="Create Post"]')
    publish_feed_btn = (AppiumBy.XPATH, '//android.widget.TextView[@text="Publish"]')

    select_viewer_btn = (AppiumBy.XPATH, '//android.widget.TextView[@text="Please choose"]')
    feed_content_input = (AppiumBy.XPATH, '//android.widget.EditText[@text="Write your update here"]')

    add_image_btn = (AppiumBy.XPATH, '(//com.horcrux.svg.PathView)[3]')
    attack_file_btn = (AppiumBy.XPATH, '(//com.horcrux.svg.PathView)[4]')


class objects_viewer_selection_screen(object):
    choose_your_viewers_lbl = (AppiumBy.XPATH, '//android.widget.TextView[@text="Choose your viewers"]')
    viewer_top_level_ddl = (AppiumBy.XPATH, '//android.widget.TextView[@text="Choose your viewers"]//parent::android.view.ViewGroup//android.widget.ScrollView/android.view.ViewGroup')
    select_viewer_chk = (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="toggle_undefined"]')

    viewer_selection_section = (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="ExpandedItem_ContentContainer"]')




class activity_feed_create_post_screen(base_screen):
    def __init__(self, driver):
        super().__init__(driver)

    def get_create_feed_title(self):
        return self.get_element_by_locator(objects_activity_feed_create_post_screen.create_post_lbl)

    def get_select_viewer_btn(self):
        return self.get_element_by_locator(objects_activity_feed_create_post_screen.select_viewer_btn)

    def get_feed_content_input(self):
        return self.get_element_by_locator(objects_activity_feed_create_post_screen.feed_content_input)

    def get_publish_feed_btn(self):
        return self.get_element_by_locator(objects_activity_feed_create_post_screen.publish_feed_btn)

    # Action
    def action_tap_select_viewer(self):
        return self.action_tap(self.get_select_viewer_btn())

    def action_type_feed_content(self, value):
        return self.action_type(self.get_feed_content_input(), value=value)

    # Func
    def func_create_a_feed(self, is_image: bool, is_attack: bool):
        try:
            self.action_tap_select_viewer()
        except Exception:
            raise Exception

    def func_fill_all_checklist_items_from_1_screen(self):
        try:
            items = self.get_checklist_items_txt()
            list_answer = []
            for item in items:
                self.action_swipe_up_to_element(item)
                element_text = self.get_text(item)
                if element_text == 'Yes':
                    self.action_tap(item)
        except Exception:
            raise Exception

    def func_fill_all_input_items_from_1_screen(self):
        try:
            input_items = self.get_input_items_txt()
            for item in input_items:
                self.action_swipe_up_to_element(item)
                self.action_type(item, '40')
        except Exception:
            raise Exception

    # Verify
    def verify(self):
        pass

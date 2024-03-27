from utilities import data_provider
from pages.base_screen import base_screen
from utilities.logic_utils import Logic_Util
from utilities.log_utils import action_log_decorator
from appium.webdriver.common.appiumby import AppiumBy


class objects_activity_feed_create_post_screen(object):
    create_post_lbl = (AppiumBy.XPATH, '//android.widget.TextView[@text="Create Post"]')
    publish_feed_btn = (AppiumBy.XPATH, '//android.widget.TextView[@text="Publish"]')

    select_viewer_btn = (AppiumBy.XPATH, '//android.widget.TextView[@text="Please choose"]')
    feed_content_input = (AppiumBy.XPATH, '//android.widget.EditText')

    add_image_btn = (AppiumBy.XPATH, '(//com.horcrux.svg.PathView)[3]')
    attack_file_btn = (AppiumBy.XPATH, '(//com.horcrux.svg.PathView)[4]')


class objects_viewer_selection_screen(object):
    choose_your_viewers_lbl = (AppiumBy.XPATH, '//android.widget.TextView[@text="Choose your viewers"]')
    viewer_top_level_ddl = (AppiumBy.XPATH,
                            '//android.widget.TextView[@text="Choose your viewers"]//parent::android.view.ViewGroup//android.widget.ScrollView/android.view.ViewGroup')
    select_viewer_chk = (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="toggle_undefined"]')
    viewer_selection_section = (
        AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="ExpandedItem_ContentContainer"]')
    done_btn = (AppiumBy.XPATH, '//android.widget.TextView[@text="Done"]')


@action_log_decorator
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

    def get_choose_your_viewers_lbl(self):
        return self.get_element_by_locator(objects_viewer_selection_screen.choose_your_viewers_lbl)

    def get_select_viewer_chk(self):
        return self.get_element_by_locator(objects_viewer_selection_screen.select_viewer_chk)

    def get_viewer_selection_section(self):
        return self.get_element_by_locator(objects_viewer_selection_screen.viewer_selection_section)

    def get_viewer_top_level_ddl(self):
        return self.get_element_by_locator(objects_viewer_selection_screen.viewer_top_level_ddl)

    def get_done_btn(self):
        return self.get_element_by_locator(objects_viewer_selection_screen.done_btn)

    # Action
    def action_tap_select_viewer(self):
        return self.action_tap(self.get_select_viewer_btn())

    def action_type_feed_content(self, value):
        return self.action_type(self.get_feed_content_input(), value=value)
        # to-do: implement a new function to allow to input a long text

    def action_tap_top_viewer_group(self):
        return self.action_tap(self.get_viewer_top_level_ddl())

    def action_tap_viewer_chk(self):
        return self.action_tap(self.get_select_viewer_chk())

    def action_tap_done_btn(self):
        return self.action_tap(self.get_done_btn())

    def action_tap_publish_feed_btn(self):
        return self.action_tap(self.get_publish_feed_btn())

    # Assert
    def assert_select_viewer_screen_is_shown(self):
        assert self.is_element_present(self.get_choose_your_viewers_lbl())

    # Func
    def func_create_a_feed(self, is_image: bool, is_attack: bool, username):
        try:
            self.action_tap_select_viewer()
            self.assert_select_viewer_screen_is_shown()
            self.action_tap_top_viewer_group()
            self.action_tap_viewer_chk()
            self.action_tap_done_btn()
            feed_content = ''.join((Logic_Util.id_generator() + '_', data_provider.get_feed_data("pure")[0][0]))
            self.action_type_feed_content(feed_content)
            self.action_tap_publish_feed_btn()

        except Exception:
            raise Exception

    # Verify
    def verify(self):
        pass

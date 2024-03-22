from pages.base_screen import base_screen
from appium.webdriver.common.appiumby import AppiumBy

from utilities.log_utils import action_log_decorator


class objects_activity_feed_screen(object):
    feed_bottom_bar_btn = (AppiumBy.ID, "FEED")
    activity_feed_screen_title_txt = (AppiumBy.XPATH, '//android.view.View[@text="Activity Feed"]')
    feed_notification_btn = (AppiumBy.XPATH,
                             '(//android.view.View[@text="Activity Feed"]/parent::android.view.ViewGroup/following-sibling::android.view.ViewGroup//com.horcrux.svg.CircleView)[1]')
    add_new_feed_btn = (AppiumBy.XPATH,
                        '(//android.view.View[@text="Activity Feed"]/parent::android.view.ViewGroup/following-sibling::android.view.ViewGroup//com.horcrux.svg.CircleView)[2]')

    all_feed_top_menu_lbl = (AppiumBy.XPATH, '//android.widget.TextView[@text="ALL FEEDS"]')
    my_post_top_menu_lbl = (AppiumBy.XPATH, '//android.widget.TextView[@text="MY POSTS"]')
    groups_top_menu_lbl = (AppiumBy.XPATH, '//android.widget.TextView[@text="GROUPS"]')

    feed_content_sections = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup')
    first_section_of_feed = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]//android.widget.TextView')


@action_log_decorator
class activity_feed_screen(base_screen):
    def __init__(self, driver):
        super().__init__(driver)

    def get_feed_bottom_bar_btn(self):
        return self.get_element_by_locator(objects_activity_feed_screen.feed_bottom_bar_btn)

    def get_add_new_feed_btn(self):
        return self.get_element_by_locator(objects_activity_feed_screen.add_new_feed_btn)

    # Action
    def action_tap_feed_bottom_bar_btn(self):
        return self.action_tap(self.get_feed_bottom_bar_btn())

    def action_tap_add_new_feed_btn(self):
        return self.action_tap(self.get_add_new_feed_btn())

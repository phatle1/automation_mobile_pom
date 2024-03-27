from utilities import data_provider
from pages.base_screen import base_screen
from utilities.logic_utils import Logic_Util
from utilities.log_utils import action_log_decorator
from appium.webdriver.common.appiumby import AppiumBy


class objects_activity_feed_screen(object):
    # af = activity_feed
    af_bottom_bar_btn = (AppiumBy.ID, "FEED")
    af_screen_title_txt = (AppiumBy.XPATH, '//android.view.View[@text="Activity Feed"]')
    af_notification_btn = (AppiumBy.XPATH,
                           '(//android.view.View[@text="Activity Feed"]/parent::android.view.ViewGroup/following-sibling::android.view.ViewGroup//com.horcrux.svg.CircleView)[1]')
    af_add_new_feed_btn = (AppiumBy.XPATH,
                           '(//android.view.View[@text="Activity Feed"]/parent::android.view.ViewGroup/following-sibling::android.view.ViewGroup//com.horcrux.svg.CircleView)[2]')

    af_all_feed_top_menu_lbl = (AppiumBy.XPATH, '//android.widget.TextView[@text="ALL FEEDS"]')
    af_my_post_top_menu_lbl = (AppiumBy.XPATH, '//android.widget.TextView[@text="MY POSTS"]')
    af_groups_top_menu_lbl = (AppiumBy.XPATH, '//android.widget.TextView[@text="GROUPS"]')

    af_content_sections = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup')
    af_first_section_of_feed = (AppiumBy.XPATH,
                                '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]//android.widget.TextView')
    af_feed_owner_at_first_section = (AppiumBy.XPATH,
                                      '(//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]//android.widget.TextView)[2]')
    af_feed_content_at_first_section = (AppiumBy.XPATH,
                                        '(//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]//android.widget.TextView)[4]')


class objects_activity_feed_create_post_screen(object):
    # afcp = activity_feed_create_post
    afcp_create_post_lbl = (AppiumBy.XPATH, '//android.widget.TextView[@text="Create Post"]')
    afcp_publish_feed_btn = (AppiumBy.XPATH, '//android.widget.TextView[@text="Publish"]')

    afcp_select_viewer_btn = (AppiumBy.XPATH, '//android.widget.TextView[@text="Please choose"]')
    afcp_content_input = (AppiumBy.XPATH, '//android.widget.EditText')

    afcp_add_image_btn = (AppiumBy.XPATH, '(//com.horcrux.svg.PathView)[3]')
    afcp_attack_file_btn = (AppiumBy.XPATH, '(//com.horcrux.svg.PathView)[4]')


class objects_viewer_selection_screen(object):
    # vs = viewer_selection
    vs_choose_your_viewers_lbl = (AppiumBy.XPATH, '//android.widget.TextView[@text="Choose your viewers"]')
    vs_viewer_top_level_ddl = (AppiumBy.XPATH,
                               '//android.widget.TextView[@text="Choose your viewers"]//parent::android.view.ViewGroup//android.widget.ScrollView/android.view.ViewGroup')
    vs_select_viewer_chk = (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="toggle_undefined"]')
    vs_section = (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="ExpandedItem_ContentContainer"]')
    vs_done_btn = (AppiumBy.XPATH, '//android.widget.TextView[@text="Done"]')


@action_log_decorator
class activity_feed_screen(base_screen):
    def __init__(self, driver):
        super().__init__(driver)

    def get_feed_bottom_bar_btn(self):
        return self.get_element_by_locator(objects_activity_feed_screen.af_bottom_bar_btn)

    def get_add_new_feed_btn(self):
        return self.get_element_by_locator(objects_activity_feed_screen.af_add_new_feed_btn)

    def get_af_feed_owner(self):
        return self.get_element_by_locator(objects_activity_feed_screen.af_feed_owner_at_first_section)

    def get_af_feed_content(self):
        return self.get_element_by_locator(objects_activity_feed_screen.af_feed_content_at_first_section)

    def get_af_all_feed_top_menu_lbl(self):
        return self.get_element_by_locator(objects_activity_feed_screen.af_all_feed_top_menu_lbl)

    # Action
    def action_tap_feed_bottom_bar_btn(self):
        return self.action_tap(self.get_feed_bottom_bar_btn())

    def action_tap_add_new_feed_btn(self):
        return self.action_tap(self.get_add_new_feed_btn())

    def get_create_feed_title(self):
        return self.get_element_by_locator(objects_activity_feed_create_post_screen.afcp_create_post_lbl)

    def get_select_viewer_btn(self):
        return self.get_element_by_locator(objects_activity_feed_create_post_screen.afcp_select_viewer_btn)

    def get_feed_content_input(self):
        return self.get_element_by_locator(objects_activity_feed_create_post_screen.afcp_content_input)

    def get_publish_feed_btn(self):
        return self.get_element_by_locator(objects_activity_feed_create_post_screen.afcp_publish_feed_btn)

    def get_choose_your_viewers_lbl(self):
        return self.get_element_by_locator(objects_viewer_selection_screen.vs_choose_your_viewers_lbl)

    def get_select_viewer_chk(self):
        return self.get_element_by_locator(objects_viewer_selection_screen.vs_select_viewer_chk)

    def get_viewer_selection_section(self):
        return self.get_element_by_locator(objects_viewer_selection_screen.vs_section)

    def get_viewer_top_level_ddl(self):
        return self.get_element_by_locator(objects_viewer_selection_screen.vs_viewer_top_level_ddl)

    def get_done_btn(self):
        return self.get_element_by_locator(objects_viewer_selection_screen.vs_done_btn)

    # Action
    def action_tap_select_viewer(self):
        return self.action_tap(self.get_select_viewer_btn())

    def action_type_feed_content(self, value):
        return self.action_type(self.get_feed_content_input(), value=value)
        # to-do: implement a new function to allow to input a long text

    def action_tap_top_viewer_group(self):
        self.assert_select_viewer_screen_is_shown()
        return self.action_tap(self.get_viewer_top_level_ddl())

    def action_tap_viewer_chk(self):
        return self.action_tap(self.get_select_viewer_chk())

    def action_tap_done_btn(self):
        return self.action_tap(self.get_done_btn())

    def action_tap_publish_feed_btn(self):
        self.action_tap(self.get_publish_feed_btn())
        self.wait_until_element_to_be_visible(self.get_af_all_feed_top_menu_lbl())

    # Assert
    def assert_select_viewer_screen_is_shown(self):
        assert self.is_element_present(self.get_choose_your_viewers_lbl())

    # Func
    def func_create_a_feed(self, is_image: bool, is_attack: bool, user_details: dict):
        try:
            self.action_tap_select_viewer()
            self.action_tap_top_viewer_group()
            self.action_tap_viewer_chk()
            self.action_tap_done_btn()
            feed_id = 'id_' + Logic_Util.id_generator()
            feed_content = data_provider.get_feed_data("pure")[0][0]
            feed = ''.join((feed_id + '_', feed_content))
            self.action_type_feed_content(feed)
            self.action_tap_publish_feed_btn()
            user_full_name = f"{user_details['First Name']} {user_details['Last Name']}"
            self.verify_a_feed_is_added_successfully(user_full_name, feed_id)

        except Exception:
            raise Exception

    # Verify
    def verify(self):
        pass

    # Verify
    def verify_a_feed_is_added_successfully(self, exp_feed_owner, exp_feed_content):
        actual_feed_owner = self.get_text(self.get_af_feed_owner())
        actual_feed_content = self.get_text(self.get_af_feed_content())
        assert exp_feed_owner.__eq__(actual_feed_owner)
        assert exp_feed_content in actual_feed_content

    # Func

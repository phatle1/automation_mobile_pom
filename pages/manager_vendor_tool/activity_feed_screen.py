from pages.base_screen import base_screen
from appium.webdriver.common.appiumby import AppiumBy


class objects_activity_feed_screen(object):
    checklist_bottom_bar_btn = (AppiumBy.ID, "FEED")
    activity_feed_screen_title_txt = (AppiumBy.XPATH, '//android.view.View[@text="Activity Feed"]')
    feed_notification_btn = (AppiumBy.XPATH, '(//android.view.View[@text="Activity Feed"]/parent::android.view.ViewGroup/following-sibling::android.view.ViewGroup//com.horcrux.svg.CircleView)[1]')
    add_new_feed_btn = (AppiumBy.XPATH, '(//android.view.View[@text="Activity Feed"]/parent::android.view.ViewGroup/following-sibling::android.view.ViewGroup//com.horcrux.svg.CircleView)[2]')

    all_feed_top_menu_lbl = (AppiumBy.XPATH, '//android.widget.TextView[@text="ALL FEEDS"]')
    my_post_top_menu_lbl = (AppiumBy.XPATH, '//android.widget.TextView[@text="MY POSTS"]')
    groups_top_menu_lbl = (AppiumBy.XPATH, '//android.widget.TextView[@text="GROUPS"]')


class routines_screen(base_screen):
    def __init__(self, driver):
        super().__init__(driver)

    def get_checklist_bottom_bar_btn(self):
        return self.get_element_by_locator(objects_checklist_screen.checklist_bottom_bar_btn)

    def get_current_checklist_lbl(self):
        return self.get_element_by_locator(objects_checklist_screen.current_checklist_lbl)

    def get_checklist_history_lbl(self):
        return self.get_element_by_locator(objects_checklist_screen.checklist_history_lbl)

    def get_routine_by_name(self, routine_name):
        return self.get_element_by_locator(objects_checklist_screen.routine_by_name(routine_name))

    def get_all_current_routine_items_lbl(self):
        return self.get_elements_by_locator(objects_checklist_screen.all_current_routine_items_lbl)

    def get_checklist_item_top_menu_lbl(self):
        return self.get_elements_by_locator(objects_checklist_screen.checklist_item_top_menu_lbl)

    def get_submit_routine_btn(self):
        return self.get_elements_by_locator(objects_checklist_screen.submit_routine_btn)

    def get_back_to_main_check_list_btn(self):
        return self.get_element_by_locator(objects_checklist_screen.back_to_main_check_list_btn)

    def get_checklist_items_txt(self):
        return self.get_elements_by_locator(objects_checklist_screen.checklist_items_txt)

    def get_input_items_txt(self):
        return self.get_elements_by_locator(objects_checklist_screen.input_txt)

    # Action
    def action_select_routine_screen(self):
        return self.action_tap(self.get_checklist_bottom_bar_btn())

    def action_check_if_user_already_in_a_shift(self) -> bool:
        routine_btn = self.get_elements_by_locator(objects_checklist_screen.checklist_bottom_bar_btn)
        flag = True if len(routine_btn) > 0 else False
        return flag

    def action_tap_on_back_to_main_check_list_btn(self):
        return self.action_tap(self.get_back_to_main_check_list_btn())

    def action_swipe_up_to_element(self, *locator):
        self.swipe_vertical_to_element(*locator)

    # Func
    def func_fill_all_checklist_items(self):
        try:
            self.action_select_routine_screen()
            main_routines = self.get_all_current_routine_items_lbl()
            for routine in main_routines:
                self.action_tap(routine)
                checklist_items = self.get_checklist_item_top_menu_lbl()
                for item in checklist_items:
                    self.action_tap(item)
                    self.func_fill_all_checklist_items_from_1_screen()
                    self.func_fill_all_input_items_from_1_screen()
                    self.action_swipe_up_to_element(self.get_submit_routine_btn())

                self.action_tap_on_back_to_main_check_list_btn()
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

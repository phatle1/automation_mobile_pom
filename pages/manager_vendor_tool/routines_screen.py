from pages.base_screen import base_screen
from appium.webdriver.common.appiumby import AppiumBy


class objects_checklist_screen(object):
    checklist_bottom_bar_btn = (AppiumBy.ID, "CHECKLISTS")
    current_checklist_lbl = (AppiumBy.XPATH, '//android.widget.TextView[@text="CURRENT"]')
    checklist_history_lbl = (AppiumBy.XPATH, '//android.widget.TextView[@text="HISTORY"]')

    # checklist items
    all_current_routine_items_lbl = (AppiumBy.XPATH,
                                  '((//android.view.ViewGroup[@resource-id="RoutineGroup_RoutineGroupItems"])[1]//*[contains(@resource-id,"RoutineGroupItem@")])/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.TextView[1]')
    checklist_item_top_menu_lbl = (AppiumBy.XPATH, '//android.widget.HorizontalScrollView//android.widget.TextView')

    @staticmethod
    def routine_by_name(routine_name):
        # Setup
        # Prep
        # Mid Shift
        # Review
        return AppiumBy.XPATH, f'(//android.view.ViewGroup[@resource-id="RoutineGroup_RoutineGroupItems"])[1]//android.widget.TextView[@text="{routine_name}"]'


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

    # Action
    def action_select_routine_screen(self):
        return self.action_tap(self.get_checklist_bottom_bar_btn())

    def func_fill_all_checklist_items(self):
        self.action_select_routine_screen()
        for main_routines in self.get_all_current_routine_items_lbl():
            self.action_tap(main_routines)
            for checklist_items in self.get_checklist_item_top_menu_lbl():
                self.action_tap(checklist_items)

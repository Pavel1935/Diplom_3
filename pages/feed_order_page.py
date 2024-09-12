import allure
from locators.feed_order_locator import FeedOrderLocators
from locators.main_function_locator import MainFunctionLocators
from locators.personal_account_locator import PersonalAccountLocators
from pages.base_page import BasePage


class FeedOrderPage(BasePage):
    @allure.step('Клик на заказ')
    def click_on_feed_order_button(self):
        browser_name = self.driver.capabilities['browserName']
        self.click_on_element(MainFunctionLocators.FEED_ORDER_BUTTON)
        if browser_name == 'firefox':
            self.click_virt_mouse(MainFunctionLocators.FEED_ORDER_BUTTON)
        orders = self.find_elements_located(FeedOrderLocators.ORDER_LIST)
        last_order = orders[-1]
        last_order.click()
        return self.get_text(FeedOrderLocators.ORDER_TITLE)

    @allure.step('Заказы из истории отображаются в ленте')
    def order_history_in_feed_order(self, email, password):
        browser_name = self.driver.capabilities['browserName']
        if browser_name == 'firefox':
            self.click_virt_mouse(PersonalAccountLocators.ACCOUNT_BUTTON)
        self.click_on_element(PersonalAccountLocators.ACCOUNT_BUTTON)
        self.past_input_text(PersonalAccountLocators.EMAIL, email)
        self.past_input_text(PersonalAccountLocators.PASSWORD, password)
        self.click_on_element(PersonalAccountLocators.LOGIN_BUTTON)
        self.drag_and_drop(MainFunctionLocators.KRATORNAYA_BUTTON, MainFunctionLocators.MENU_ORDER)
        self.click_on_element(PersonalAccountLocators.BUTTON_ORDER)
        self.click_with_retry(FeedOrderLocators.CLOSE_ID_ORDER_BUTTON)
        self.click_on_element(PersonalAccountLocators.ACCOUNT_BUTTON)
        if browser_name == 'firefox':
            self.click_virt_mouse(PersonalAccountLocators.ACCOUNT_BUTTON)
        self.click_on_element(PersonalAccountLocators.ORDER_HISTORY_BUTTON)
        el_1 = self.get_text_visibility_of_all_element(FeedOrderLocators.FIRST_ORDER_HISTORY)
        self.click_on_element(MainFunctionLocators.FEED_ORDER_BUTTON)
        if browser_name == 'firefox':
            self.click_virt_mouse(MainFunctionLocators.FEED_ORDER_BUTTON)
        el_2 = self.get_text(FeedOrderLocators.FIRST_ORDER_FEED)
        return el_1, el_2


    @allure.step('создаем заказ и счетчик "за все время" увеличивается')
    def create_order_completed_for_all_time_increases(self, email, password):
            browser_name = self.driver.capabilities['browserName']
            self.click_on_element(PersonalAccountLocators.ACCOUNT_BUTTON)
            if browser_name == 'firefox':
                self.click_virt_mouse(PersonalAccountLocators.ACCOUNT_BUTTON)
            self.past_input_text(PersonalAccountLocators.EMAIL, email)
            self.past_input_text(PersonalAccountLocators.PASSWORD, password)
            self.click_on_element(PersonalAccountLocators.LOGIN_BUTTON)
            self.click_on_element(MainFunctionLocators.FEED_ORDER_BUTTON)
            if browser_name == 'firefox':
                self.click_virt_mouse(MainFunctionLocators.FEED_ORDER_BUTTON)
            completed_all_time = self.get_text_visibility_of_all_element(FeedOrderLocators.COUNTER_HISTORY)
            self.click_on_element(MainFunctionLocators.KONSTRUKTOR_BUTTON)
            if browser_name == 'firefox':
                self.click_virt_mouse(MainFunctionLocators.KONSTRUKTOR_BUTTON)
            self.drag_and_drop(MainFunctionLocators.KRATORNAYA_BUTTON, MainFunctionLocators.MENU_ORDER)
            self.click_on_element(PersonalAccountLocators.BUTTON_ORDER)
            self.click_with_retry(FeedOrderLocators.CLOSE_ID_ORDER_BUTTON)
            self.click_on_element(MainFunctionLocators.FEED_ORDER_BUTTON)
            if browser_name == 'firefox':
                self.click_virt_mouse(MainFunctionLocators.FEED_ORDER_BUTTON)
            completed_all_time_1 = self.get_text_visibility_of_all_element(FeedOrderLocators.COUNTER_HISTORY)
            return completed_all_time, completed_all_time_1

    @allure.step('создаем заказ и его номер появился в "выполненно за сегодня"')
    def create_order_completed_today(self, email, password):
        browser_name = self.driver.capabilities['browserName']
        self.click_on_element(PersonalAccountLocators.ACCOUNT_BUTTON)
        if browser_name == 'firefox':
            self.click_virt_mouse(PersonalAccountLocators.ACCOUNT_BUTTON)
        self.past_input_text(PersonalAccountLocators.EMAIL, email)
        self.past_input_text(PersonalAccountLocators.PASSWORD, password)
        self.click_on_element(PersonalAccountLocators.LOGIN_BUTTON)
        self.click_on_element(MainFunctionLocators.FEED_ORDER_BUTTON)
        if browser_name == 'firefox':
            self.click_virt_mouse(MainFunctionLocators.FEED_ORDER_BUTTON)
        completed_today = self.get_text_visibility_of_all_element(FeedOrderLocators.COUNTER_TODAY)
        self.click_on_element(MainFunctionLocators.KONSTRUKTOR_BUTTON)
        self.drag_and_drop(MainFunctionLocators.KRATORNAYA_BUTTON, MainFunctionLocators.MENU_ORDER)
        self.click_on_element(PersonalAccountLocators.BUTTON_ORDER)
        self.click_with_retry(FeedOrderLocators.CLOSE_ID_ORDER_BUTTON)
        self.click_on_element(MainFunctionLocators.FEED_ORDER_BUTTON)
        if browser_name == 'firefox':
            self.click_virt_mouse(MainFunctionLocators.FEED_ORDER_BUTTON)
        completed_today_1 = self.get_text_visibility_of_all_element(FeedOrderLocators.COUNTER_TODAY)
        return completed_today, completed_today_1


    @allure.step('оформленный заказ появился в разделе "в работе"')
    def after_placing_order_number_appears_in_work(self, email, password):
        browser_name = self.driver.capabilities['browserName']
        self.click_on_element(PersonalAccountLocators.ACCOUNT_BUTTON)
        if browser_name == 'firefox':
            self.click_virt_mouse(PersonalAccountLocators.ACCOUNT_BUTTON)
        self.past_input_text(PersonalAccountLocators.EMAIL, email)
        self.past_input_text(PersonalAccountLocators.PASSWORD, password)
        self.click_on_element(PersonalAccountLocators.LOGIN_BUTTON)
        self.drag_and_drop(MainFunctionLocators.KRATORNAYA_BUTTON, MainFunctionLocators.MENU_ORDER)
        self.click_on_element(PersonalAccountLocators.BUTTON_ORDER)
        ID_ORDER = self.get_text_visibility_of_all_element(FeedOrderLocators.CREATE_ORDER_TYTLLE)
        self.click_with_retry(FeedOrderLocators.CLOSE_ID_ORDER_BUTTON)
        self.click_on_element(MainFunctionLocators.FEED_ORDER_BUTTON)
        if browser_name == 'firefox':
            self.click_virt_mouse(MainFunctionLocators.FEED_ORDER_BUTTON)
        ORDER_IN_PROG = self.get_text_visibility_of_all_element(FeedOrderLocators.ORDER_IN_PROGRESS)
        return ID_ORDER, ORDER_IN_PROG



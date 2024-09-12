import allure
from locators.main_function_locator import MainFunctionLocators
from locators.personal_account_locator import PersonalAccountLocators
from pages.base_page import BasePage


class MainFunctionPage(BasePage):

    @allure.step('клик на кнопку "конструктор"')
    def click_on_constructor_button(self):
        browser_name = self.driver.capabilities['browserName']
        if browser_name == 'chrome':
            self.click_on_element(PersonalAccountLocators.ACCOUNT_BUTTON)
        elif browser_name == 'firefox':
            self.click_virt_mouse(MainFunctionLocators.FEED_ORDER_BUTTON)
        self.click_on_element(MainFunctionLocators.KONSTRUKTOR_BUTTON)

    @allure.step('клик на кнопку "лента заказов"')
    def click_on_feed_order_button(self):
        browser_name = self.driver.capabilities['browserName']
        if browser_name == 'chrome':
            self.click_on_element(MainFunctionLocators.FEED_ORDER_BUTTON)
        elif browser_name == 'firefox':
            self.click_virt_mouse(MainFunctionLocators.FEED_ORDER_BUTTON)


    @allure.step('клик на ингредиент и появляется окно с деталями')
    def open_window_with_details(self):
        browser_name = self.driver.capabilities['browserName']
        if browser_name == 'chrome':
            self.click_on_element(MainFunctionLocators.KRATORNAYA_BUTTON)
        elif browser_name == 'firefox':
            self.click_virt_mouse(MainFunctionLocators.KRATORNAYA_BUTTON)
        return self.get_text(MainFunctionLocators.INGREDIENT_DETALIS)

    @allure.step('всплывающее окно закрывается крестиком')
    def close_window_with_details(self):
        browser_name = self.driver.capabilities['browserName']
        if browser_name == 'chrome':
            self.click_on_element(MainFunctionLocators.KRATORNAYA_BUTTON)
        elif browser_name == 'firefox':
            self.click_virt_mouse(MainFunctionLocators.KRATORNAYA_BUTTON)
        self.click_on_element(MainFunctionLocators.CLOSE_MODAL_WINDOW)
        if browser_name == 'chrome':
            self.click_on_element(MainFunctionLocators.KRATORNAYA_BUTTON)
        elif browser_name == 'firefox':
            self.click_virt_mouse(MainFunctionLocators.KRATORNAYA_BUTTON)
        return self.get_text(MainFunctionLocators.INGREDIENT_DETALIS)

    @allure.step('при добавлении ингредиента увеличивается каунтер')
    def counter_ingredient_up(self):
        self.drag_and_drop(MainFunctionLocators.KRATORNAYA_BUTTON, MainFunctionLocators.MENU_ORDER)
        return self.get_text(MainFunctionLocators.AMMOUNT_ORDER)

    @allure.step('оформление заказа залогиненым пользователем')
    def logged_user_can_place_an_order(self, email, password):
        browser_name = self.driver.capabilities['browserName']
        if browser_name == 'chrome':
            self.click_on_element(PersonalAccountLocators.ACCOUNT_BUTTON)
        elif browser_name == 'firefox':
            self.click_virt_mouse(PersonalAccountLocators.ACCOUNT_BUTTON)
        self.past_input_text(PersonalAccountLocators.EMAIL, email)
        self.past_input_text(PersonalAccountLocators.PASSWORD, password)
        self.click_on_element(PersonalAccountLocators.LOGIN_BUTTON)
        self.drag_and_drop(MainFunctionLocators.KRATORNAYA_BUTTON, MainFunctionLocators.MENU_ORDER)
        self.click_on_element(PersonalAccountLocators.BUTTON_ORDER)
        return self.get_text(MainFunctionLocators.ID_ORDER)











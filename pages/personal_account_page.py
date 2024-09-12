import allure
from locators.personal_account_locator import PersonalAccountLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    @allure.step('клик на "личный кабинет"')
    def click_on_account_button(self):
        self.click_virt_mouse(PersonalAccountLocators.ACCOUNT_BUTTON)
        return self.get_text(PersonalAccountLocators.LOGIN_TYTLLE)

    @allure.step('Клик на "историю заказов"')
    def click_on_order_history(self, email, password):
        browser_name = self.driver.capabilities['browserName']
        self.click_on_element(PersonalAccountLocators.ACCOUNT_BUTTON)
        if browser_name == 'firefox':
            self.click_virt_mouse(PersonalAccountLocators.ACCOUNT_BUTTON)
        self.past_input_text(PersonalAccountLocators.EMAIL, email)
        self.past_input_text(PersonalAccountLocators.PASSWORD, password)
        self.click_on_element(PersonalAccountLocators.LOGIN_BUTTON)
        self.click_on_element(PersonalAccountLocators.ACCOUNT_BUTTON)
        if browser_name == 'firefox':
            self.click_virt_mouse(PersonalAccountLocators.ACCOUNT_BUTTON)
        self.click_virt_mouse(PersonalAccountLocators.ACCOUNT_BUTTON)
        self.click_on_element(PersonalAccountLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Клик на кнопку выход из акаунта')
    def click_on_exit_button(self, email, password):
        browser_name = self.driver.capabilities['browserName']
        self.click_on_element(PersonalAccountLocators.ACCOUNT_BUTTON)
        if browser_name == 'firefox':
            self.click_virt_mouse(PersonalAccountLocators.ACCOUNT_BUTTON)
        self.past_input_text(PersonalAccountLocators.EMAIL, email)
        self.past_input_text(PersonalAccountLocators.PASSWORD, password)
        self.click_on_element(PersonalAccountLocators.LOGIN_BUTTON)
        self.click_on_element(PersonalAccountLocators.ACCOUNT_BUTTON)
        if browser_name == 'firefox':
            self.click_virt_mouse(PersonalAccountLocators.ACCOUNT_BUTTON)
        self.click_on_element(PersonalAccountLocators.EXIT_BUTTON)
        return self.get_text(PersonalAccountLocators.LOGIN_TYTLLE)








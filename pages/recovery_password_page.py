import allure
from data import Constants
from locators.personal_account_locator import PersonalAccountLocators
from pages.base_page import BasePage
from locators.recovery_password_locator import RecoveryPasswordLocators


class RecoveryPasswordPage(BasePage):

    @allure.step('Клик на кнопку "восстановить пароль"')
    def click_on_recovery_button(self):
        self.click_virt_mouse(RecoveryPasswordLocators.ACCOUNT_BUTTON)
        self.click_on_element(RecoveryPasswordLocators.RECOVERY_PASS_BUTTON)
        return self.get_text(RecoveryPasswordLocators.RECOVERY_TITLE)

    @allure.step('ввода почты по кнопке "восстановить"')
    def enter_email(self):
        self.click_virt_mouse(RecoveryPasswordLocators.ACCOUNT_BUTTON)
        self.click_on_element(RecoveryPasswordLocators.RECOVERY_PASS_BUTTON)
        self.past_input_text(RecoveryPasswordLocators.RECOVERY_INPUT, Constants.EMAIL)
        self.click_on_element(RecoveryPasswordLocators.RECOVERY_BUTTON)
        return self.get_text(RecoveryPasswordLocators.SAVE_BUTTON)


    @allure.step('клик на глазик делает поле активным и подсвечивает его')
    def click_on_eye_button(self):
        browser_name = self.driver.capabilities['browserName']
        self.click_on_element(PersonalAccountLocators.ACCOUNT_BUTTON)
        if browser_name == 'firefox':
            self.click_virt_mouse(PersonalAccountLocators.ACCOUNT_BUTTON)
        self.click_on_element(RecoveryPasswordLocators.RECOVERY_PASS_BUTTON)
        self.past_input_text(RecoveryPasswordLocators.RECOVERY_INPUT, Constants.EMAIL)
        self.click_on_element(RecoveryPasswordLocators.RECOVERY_BUTTON)
        self.click_on_element(RecoveryPasswordLocators.EYE_BUTTON)
        return self.get_attribute_class(RecoveryPasswordLocators.EYE_ATTRIBUTE_ACTIVE)




import allure
from data import Constants
from pages.recovery_password_page import RecoveryPasswordPage


class TestRecoveryPasswordPage:

    @allure.title('переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_click_on_recovery_button(self, driver):
        recovery_password_page = RecoveryPasswordPage(driver)
        result = recovery_password_page.click_on_recovery_button()
        assert result == 'Восстановление пароля'


    @allure.title('ввод почты и клик по кнопке «Восстановить»')
    def test_enter_mail(self, driver):
        recovery_password_page = RecoveryPasswordPage(driver)
        result = recovery_password_page.enter_email()
        assert result == 'Сохранить'

    @allure.title('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_on_eye_button(self, driver):
        recovery_password_page = RecoveryPasswordPage(driver)
        expected_class = recovery_password_page.click_on_eye_button()
        assert expected_class == Constants.ATTRIBUTE
import allure
from pages.personal_account_page import PersonalAccountPage



class TestPersonalAccountPage:

    @allure.title('переход по клику на «Личный кабинет»')
    def test_click_on_account_button(self, driver):
        personal_account_page = PersonalAccountPage(driver)
        result = personal_account_page.click_on_account_button()
        assert result == 'Вход'

    @allure.title('переход в раздел «История заказов»')
    def test_click_on_order_history(self, driver, create_user, delete_user):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_on_order_history(
            email=create_user['email'],
            password=create_user['password']
        )
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/order-history'

    @allure.title('выход из аккаунта')
    def test_click_on_exit_button(self, driver, create_user, delete_user):
        personal_account_page = PersonalAccountPage(driver)
        result = personal_account_page.click_on_exit_button(
            email=create_user['email'],
            password=create_user['password']
        )
        assert result == 'Вход'



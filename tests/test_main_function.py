import allure
from pages.main_function_page import MainFunctionPage


class TestMainFunctionPage:
    @allure.title('переход по клику на «Конструктор»')
    def test_click_on_constructor_button(self, driver):
        test_main_function_page = MainFunctionPage(driver)
        test_main_function_page.click_on_constructor_button()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    @allure.title('переход по клику на «Лента заказов»')
    def test_click_on_fed_order_button(self, driver):
        test_main_function_page = MainFunctionPage(driver)
        test_main_function_page.click_on_feed_order_button()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/feed'

    @allure.title('если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_open_window_with_details(self, driver):
        main_function_page = MainFunctionPage(driver)
        result = main_function_page.open_window_with_details()
        assert result == 'Краторная булка N-200i'

    @allure.title('всплывающее окно закрывается кликом по крестику')
    def test_close_window_with_details(self, driver):
        main_function_page = MainFunctionPage(driver)
        result = main_function_page.close_window_with_details()
        assert result == 'Краторная булка N-200i'


    @allure.title('при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_counter_ingredient_up(self, driver):
        main_function_page = MainFunctionPage(driver)
        result = main_function_page.counter_ingredient_up()
        assert result == '2510'

    @allure.title('залогиненный пользователь может оформить заказ')
    def test_logged_user_can_place_an_order(self, driver, create_user, delete_user):
        main_function_page = MainFunctionPage(driver)
        result = main_function_page.logged_user_can_place_an_order(
            email=create_user['email'],
            password=create_user['password']
        )
        assert result == "идентификатор заказа"
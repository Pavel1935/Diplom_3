import allure
from pages.feed_order_page import FeedOrderPage


class TestFeedOrderPage:
    @allure.title('если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_on_feed_order_button(self, driver):
        feed_order_page = FeedOrderPage(driver)
        result = feed_order_page.click_on_feed_order_button()
        assert result == 'Cостав'

    @allure.title('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_order_history_in_feed_order(self, driver, create_user, delete_user):
        feed_order_page = FeedOrderPage(driver)
        el_1, el_2 = feed_order_page.order_history_in_feed_order(
            email=create_user['email'],
            password=create_user['password']
        )
        extracted_el_1 = el_1.split('\n')[-1]
        extracted_el_2 = el_2.strip()
        assert extracted_el_1 == extracted_el_2

    @allure.title('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_create_order_completed_for_all_time_increases(self, driver, create_user, delete_user):
        feed_order_page = FeedOrderPage(driver)
        completed_all_time, completed_all_time_1 =feed_order_page.create_order_completed_for_all_time_increases(
            email=create_user['email'],
            password=create_user['password']
        )

        assert completed_all_time != completed_all_time_1


    @allure.title('при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_create_order_completed_today(self, driver, create_user, delete_user):
        feed_order_page = FeedOrderPage(driver)
        completed_today, completed_today_1 = feed_order_page.create_order_completed_today(
            email=create_user['email'],
            password=create_user['password']
        )
        assert completed_today != completed_today_1

    @allure.title('после оформления заказа его номер появляется в разделе В работе')
    def test_after_placing_order_number_appears_in_work(self, driver, create_user, delete_user):
        feed_order_page = FeedOrderPage(driver)
        ID_ORDER, ORDER_IN_PROG = feed_order_page.after_placing_order_number_appears_in_work(
            email=create_user['email'],
            password=create_user['password']
        )
        extracted_el_1 = ORDER_IN_PROG.split('\n')[-1]
        extracted_el_2 = ID_ORDER.strip()
        assert extracted_el_2 in extracted_el_1
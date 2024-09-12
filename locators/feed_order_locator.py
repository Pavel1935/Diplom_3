from selenium.webdriver.common.by import By


class FeedOrderLocators:
    FEED_ORDER_BUTTON = By.XPATH, "//p[contains(text(),'Лента Заказов')]"
    # Кнопка "Лента заказов"
    FEED_ORDER_TYTLLE = By.XPATH, "//p[contains(text(),'Лента Заказов')]"
    # Заголовок "Лента заказов"
    CLOSE_ID_ORDER_BUTTON = By.XPATH, "//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"
    # Кнопка "Закрыть" и иконка "Закрыть" в модальном окне
    ORDER_LIST = By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li"
    # Список заказов
    ORDER_TITLE = By.XPATH, "//p[@class='text text_type_main-medium mb-8']"
    # Заголовок заказа
    FIRST_ORDER_HISTORY = By.XPATH, "//a[@class='OrderHistory_link__1iNby']"
    # Ссылка на первый заказ в истории заказов
    FIRST_ORDER_FEED = By.XPATH, "//div[@class='OrderHistory_dataBox__1mkxK'][1]"
    # Первый заказ в ленте заказов
    COUNTER_HISTORY = By.XPATH, "//div[contains(@class, 'undefined mb-15')]/p[contains(@class, 'OrderFeed_number__')]"
    # Количество заказов в ленте заказов
    COUNTER_TODAY = By.XPATH, "//div[@class='OrderFeed_ordersData__1L6Iv']/div[3]/p[contains(@class, 'OrderFeed_number__')]"
    # Количество заказов сегодня
    CREATE_ORDER_TYTLLE = By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']"
    # Текст модального окна создания заказа
    ORDER_IN_PROGRESS = By.XPATH, "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']"
    # Список заказов в процессе
    OVERLAY_LOCATOR = By.XPATH, "//section[@class='Modal_modal__P3_V5']//div[@class='Modal_modal_overlay__x2ZCr']"
    # Модальное окно

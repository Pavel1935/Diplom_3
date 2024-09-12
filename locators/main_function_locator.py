from selenium.webdriver.common.by import By

class MainFunctionLocators:
    KONSTRUKTOR_BUTTON = By.XPATH, "//p[contains(text(),'Конструктор')]"
    # Кнопка "Конструктор"
    FEED_ORDER_BUTTON = By.XPATH, "//p[contains(text(),'Лента Заказов')]"
    # Кнопка "Лента заказов"
    KRATORNAYA_BUTTON = By.XPATH, "//p[contains(text(),'Краторная булка N-200i')]"
    # Кнопка "Краторная булка N-200i"
    INGREDIENT_DETALIS = By.XPATH, "//p[@class='text text_type_main-medium mb-8']"
    # Текст "Детали ингредиента"
    CLOSE_MODAL_WINDOW = By.XPATH, "//section[contains(@class,'Modal_modal_opened')]//button[@type='button']"
    # Кнопка "Закрыть" в модальном окне
    AMMOUNT_ORDER = By.XPATH, "//p[@class='text text_type_digits-medium mr-3']"
    # Сумма заказа
    MENU_ORDER = By.XPATH, "//div[@class='constructor-element constructor-element_pos_top']"
    # Меню заказа
    ID_ORDER = By.XPATH, "//p[contains(text(),'идентификатор заказа')]"
    # Идентификатор заказа
from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    ACCOUNT_BUTTON = By.XPATH, "//p[contains(text(),'Личный Кабинет')]"
    # Кнопка "Личный кабинет"
    LOGIN_TYTLLE = By.XPATH, "//h2[contains(text(),'Вход')]"
    # Заголовок "Вход"
    EMAIL = By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input[@name='name']"
    # Инпут email
    PASSWORD = By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input[@name='Пароль']"
    # Инпут password
    LOGIN_BUTTON = By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
    # Кнопка "Войти"
    ORDER_HISTORY_BUTTON = By.XPATH, "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']"
    # Кнопка "История заказов"
    USER_ORDER_1 = By.XPATH, "//h2[@class='text text_type_main-medium mb-2']"
    # Первый заказ "краторный бургер" ленте заказов
    EXIT_BUTTON = By.XPATH, "//button[contains(text(),'Выход')]"
    # Кнопка "Выйти"
    MENU_ORDER = By.XPATH, "//div[@class='constructor-element constructor-element_pos_top']"
    # Меню заказа
    BUTTON_ORDER = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    # Кнопка "Оформить заказ"


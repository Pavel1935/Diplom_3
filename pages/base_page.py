from selenium.common import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.feed_order_locator import FeedOrderLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, MAIN_URL):
        return self.driver.get(MAIN_URL)

    def find_element_wait(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(locator))

    def find_element_wait_visability(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator))

    def scroll_to_element_located(self, locator):
        element = self.find_element_wait_visability(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_on_element(self, locator):
        return self.find_element_wait(locator).click()

    def format_locator(self, locator, num):
        method, loc = locator
        formatted_loc = loc.format(num=num)
        return (method, formatted_loc)

    def past_input_text(self, locator, text):
        element = self.find_element_wait(locator)
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_element_wait(locator).text

    def get_text_visibility_of_all_element(self, locator):
        return self.find_element_located(locator).text

    def find_element_located(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(
        expected_conditions.presence_of_element_located(locator))

    def find_elements_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
        expected_conditions.visibility_of_all_elements_located(locator))

    def drag_and_drop(self, locator_element_from, locator_element_to):
         from_element = self.find_element_wait(locator_element_from)
         to_element = self.find_element_wait(locator_element_to)
         ActionChains(self.driver).drag_and_drop(from_element, to_element).perform()

    def get_attribute_class(self, locator):
        return self.driver.find_element(*locator).get_attribute('class')


    def find_element_wait_visibility_of_element(self, locator, time=20):
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h2.text_type_digits-large"))
        )

    def get_order_no(self, locator):
        return self.driver.find_element_wait_visibility_of_element(*locator).get_attribute('class')

    def click_with_retry(self, locator, retries=3, wait_time=10):
        for attempt in range(retries):
            try:
                element = self.find_element_wait(locator)
                element.click()
                return
            except ElementClickInterceptedException:
                overlay_locator = (FeedOrderLocators.OVERLAY_LOCATOR)
                WebDriverWait(self.driver, wait_time).until(
                    EC.invisibility_of_element_located(overlay_locator)
                )
                if attempt == retries - 1:
                    raise

    def click_virt_mouse(self, locator):
        action = ActionChains(self.driver)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        action.click(on_element=element).perform()

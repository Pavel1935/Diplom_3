import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from data import Constants
import requests
from faker import Faker
fake = Faker()



@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    elif request.param == 'chrome':
        options = ChromeOptions()
        driver = webdriver.Chrome(options=options)
    driver.get(Constants.MAIN_URL)
    yield driver
    driver.quit()





# @pytest.fixture
# def driver():
#     driver = webdriver.Firefox()
#     driver.get(Constants.MAIN_URL)
#     yield driver
#     driver.quit()
#
# @pytest.fixture
# def driver():
#    driver = webdriver.Chrome()
#    driver.get(Constants.MAIN_URL)
#    yield driver
#    driver.quit()



@pytest.fixture
def create_user():
    user_data = {
        'email': fake.email(),
        'password': fake.password(),
        'name': fake.name()
    }
    response = requests.post(Constants.CREATE_USER_URL, json=user_data)
    user_data['token'] = response.json()['accessToken'].replace('Bearer ', '')
    return user_data

@pytest.fixture
def delete_user(create_user):
    yield
    headers = {
        'Authorization': f'Bearer {create_user["token"]}'
    }
    requests.delete(Constants.DELETE_COURIER_URL, headers=headers)


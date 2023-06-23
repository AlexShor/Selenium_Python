import pytest
import os
from selenium import webdriver
from dotenv import load_dotenv


@pytest.fixture(scope="class")
def browser():
    # print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(15)
    yield browser
    # print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="class")
def credentials():
    load_dotenv()
    EMAIL = os.getenv('EMAIL')
    PASSWORD = os.getenv('PASSWORD')
    return {'email': EMAIL, 'password': PASSWORD}


@pytest.fixture(scope="class")
def link():
    return "https://stepik.org/lesson/236895/step/1"

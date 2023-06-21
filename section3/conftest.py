import pytest
from selenium import webdriver


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
    return {'email': 'lex.shor@gmail.com', 'password': 'NM-@XeYfGrgNmP8'}


@pytest.fixture(scope="class")
def link():
    return "https://stepik.org/lesson/236895/step/1"

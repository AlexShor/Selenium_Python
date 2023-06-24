import pytest
import os
from selenium import webdriver
from dotenv import load_dotenv


# @pytest.fixture(scope="module")
def links():
    lessons = ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905']
    # lessons = ['236895', '236896']
    list_links = [f"https://stepik.org/lesson/{lesson_id}/step/1" for lesson_id in lessons]
    return list_links


@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(20)
    yield browser
    browser.quit()


@pytest.fixture()
def credentials():
    load_dotenv()
    EMAIL = os.getenv('EMAIL')
    PASSWORD = os.getenv('PASSWORD')
    return {'email': EMAIL, 'password': PASSWORD}

import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


def find_element(browser, find_by, element, action='', send_data=''):
    found_elem = browser.find_elements(find_by, element)
    if len(found_elem) == 0:
        print(f'[No Such Element by {find_by}: "{element}"]', end=' ')
        assert False, f'[No Such Element by {find_by}: "{element}"]'
    else:
        match action:
            case 'click':
                found_elem[0].click()
            case 'send_keys':
                found_elem[0].send_keys(send_data)
            case '':
                pass


class TestLogin:

    def test_open_lesson_page(self, browser, link):
        browser.get(link)

        elements = ['navbar__auth_login', 'quiz__typename']
        for elem in elements:
            find_element(browser, By.CLASS_NAME, elem)
            # found_elem = browser.find_elements(By.CLASS_NAME, elem)
            # if len(found_elem) == 0:
            #     print(f'[No Such Element: "{elem}"]', end=' ')
            #     assert False, f'[No Such Element: "{elem}"]'

    def test_open_modal_window_authorization(self, browser):
        element = 'navbar__auth_login'
        find_element(browser, By.CLASS_NAME, element, 'click')
        # found_elem = browser.find_elements(By.CLASS_NAME, element)
        # if len(found_elem) == 0:
        #     print(f'[No Such Element: "{element}"]', end=' ')
        #     assert False, f'[No Such Element: "{element}"]'
        # else:
        #     found_elem[0].click()

        element = 'modal-dialog__content'
        find_element(browser, By.CLASS_NAME, element)
        # found_elem = browser.find_elements(By.CLASS_NAME, element)
        # if len(found_elem) == 0:
        #     print(f'[No Such Element: "{element}"]', end=' ')
        #     assert False, f'[No Such Element: "{element}"]'

    def test_fill_authorization_credentials(self, browser, credentials):
        for cred_key in credentials.keys():
            element = f'id_login_{cred_key}'
            find_element(browser, By.ID, element, 'send_keys', credentials.get(cred_key))
            # found_elem = browser.find_elements(By.ID, element)
            # if len(found_elem) == 0:
            #     print(f'[No Such Element: "{element}"]', end=' ')
            #     assert False, f'[No Such Element: "{element}"]'
            # else:
            #     found_elem[0].send_keys(credentials.get(cred_key))

    def test_authorization_button(self, browser):
        element = 'sign-form__btn'
        find_element(browser, By.CLASS_NAME, element, 'click')
        # found_elem = browser.find_elements(By.CLASS_NAME, element)
        # if len(found_elem) == 0:
        #     print(f'[No Such Element: "{element}"]', end=' ')
        #     assert False, f'[No Such Element: "{element}"]'
        # else:
        #     found_elem[0].click()
        element = 'navbar__profile-toggler'
        find_element(browser, By.CLASS_NAME, element)

        time.sleep(1)



import pytest
import time
from selenium.webdriver.common.by import By


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

    def test_open_modal_window_authorization(self, browser):
        find_element(browser, By.CLASS_NAME, 'navbar__auth_login', 'click')
        find_element(browser, By.CLASS_NAME, 'modal-dialog__content')

    def test_fill_authorization_credentials(self, browser, credentials):
        for cred_key in credentials.keys():
            find_element(browser, By.ID, f'id_login_{cred_key}', 'send_keys', credentials.get(cred_key))

    def test_authorization_button(self, browser):
        find_element(browser, By.CLASS_NAME, 'sign-form__btn', 'click')
        find_element(browser, By.CLASS_NAME, 'navbar__profile-toggler')

        time.sleep(1)



import pytest
import time
import math
from selenium.webdriver.common.by import By
from conftest import links


def answer():
    return str(math.log(int(time.time())))


def error_output(text):
    print(text, end=' ')
    assert False, text


def find_element(browser, find_by, element):
    found_elem = browser.find_elements(find_by, element)
    if len(found_elem) == 0:
        error_output(f'[No Such Element by {find_by}: "{element}"]')
    else:
        return found_elem[0]


@pytest.mark.parametrize('link', links())
class TestLogin:

    def test_check_lesson(self, browser, link, credentials):

        browser.get(link)

        for elem in ['navbar__auth_login', 'quiz__typename']:
            find_element(browser, By.CLASS_NAME, elem)

        # test_open_modal_window_authorization
        find_element(browser, By.CLASS_NAME, 'navbar__auth_login').click()
        find_element(browser, By.CLASS_NAME, 'modal-dialog__content')

        # test_fill_authorization_credentials
        for cred_key in credentials.keys():
            find_element(browser, By.ID, f'id_login_{cred_key}').send_keys(credentials.get(cred_key))

        # test_authorization_button
        find_element(browser, By.CLASS_NAME, 'sign-form__btn').click()
        find_element(browser, By.CLASS_NAME, 'navbar__profile-toggler')

        # test_check_textarea_and_send_answer
        textarea = find_element(browser, By.CLASS_NAME, 'string-quiz__textarea')
        if textarea.is_enabled():
            textarea.send_keys(answer())

            # test_click_a_button_submit
            find_element(browser, By.CLASS_NAME, 'submit-submission').click()
        else:
            print(f'[Answer has already been sent]', end=' ')

        # test_check_result
        result = find_element(browser, By.CLASS_NAME, 'smart-hints__hint').text
        expected_result = 'Correct!'
        if result != expected_result:
            error_output(f'[Result text not "{expected_result}" but "{result}"]')


    # def test_open_modal_window_authorization(self, browser, link):
    #     find_element(browser, By.CLASS_NAME, 'navbar__auth_login').click()
    #     find_element(browser, By.CLASS_NAME, 'modal-dialog__content')
    #
    # def test_fill_authorization_credentials(self, browser, credentials, link):
    #     for cred_key in credentials.keys():
    #         find_element(browser, By.ID, f'id_login_{cred_key}').send_keys(credentials.get(cred_key))
    #
    # def test_authorization_button(self, browser, link):
    #     find_element(browser, By.CLASS_NAME, 'sign-form__btn').click()
    #     find_element(browser, By.CLASS_NAME, 'navbar__profile-toggler')
    #
    #     time.sleep(1)
    #
    # def test_check_textarea_and_paste_answer(self, browser, link):
    #     textarea = find_element(browser, By.CLASS_NAME, 'string-quiz__textarea')
    #     if textarea.is_enabled():
    #         textarea.send_keys(answer())
    #     else:
    #         error_output(f'[Textarea not empty]')


# class TestSendAnswer:
#
#     def test_check_textarea_and_paste_answer(self, browser, link):
#         textarea = find_element(browser, By.CLASS_NAME, 'string-quiz__textarea')
#         if textarea.is_enabled():
#             textarea.send_keys(answer())
#         else:
#             error_output(f'[Textarea not empty]')

    # def test_click_a_button_submit(self, browser):
    #     find_element(browser, By.CLASS_NAME, 'submit-submission').click()
    #
    # def test_check_result(self, browser):
    #     result = find_element(browser, By.CLASS_NAME, 'smart-hints__hint').text
    #     expected_result = 'Correct!'
    #     if result != expected_result:
    #         error_output(f'[Result text not "{expected_result}"]')
    #
    #     time.sleep(1)

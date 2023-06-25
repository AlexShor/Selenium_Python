import pytest
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

page_link = "http://suninjuly.github.io/registration"

req_input_class_names = ['first', 'second', 'third']
result_text = 'successfully'


def registration_page(link):
    browser = webdriver.Chrome()
    browser.implicitly_wait(1)
    browser.get(link)
    try:
        for class_name in req_input_class_names:
            css_selector_elem = f'div.first_block input.{class_name}'
            element = browser.find_elements(By.CSS_SELECTOR, css_selector_elem)
            assert element, f'Element not found: "{css_selector_elem}"'
            if len(element) > 0: element[0].send_keys("test")

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        return browser.find_element(By.TAG_NAME, "h1").text
    finally:
        browser.quit()


def test_registration_page_1(page='1'):
    assert result_text in registration_page(page_link + page), f"Not found text: '{result_text}'"


def test_registration_page_2(page='2'):
    assert result_text in registration_page(page_link + page), f"Not found text: '{result_text}'"


if __name__ == "__main__":

    pytest.main()

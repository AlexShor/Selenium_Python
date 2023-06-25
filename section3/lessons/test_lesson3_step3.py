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
    browser.implicitly_wait(2)
    browser.get(link)
    try:
        for class_name in req_input_class_names:
            browser.find_element(By.CSS_SELECTOR, f'div.first_block input.{class_name}').send_keys("test")
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

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/registration"


class TestRegistrationPages(unittest.TestCase):
    req_input_class_names = ['first', 'second', 'third']
    result_text = 'successfully'
    browser = webdriver.Chrome()
    browser.implicitly_wait(2)

    def test_registration_page_1(self):
        page = '1'
        self.browser.get(link + page)

        for class_name in self.req_input_class_names:
            with self.subTest(class_name=class_name):
                self.browser.find_element(By.CSS_SELECTOR, f'div.first_block input.{class_name}').send_keys("test")
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn(self.result_text, welcome_text, f"Not found text: '{self.result_text}'")

    def test_registration_page_2(self):
        page = '2'
        self.browser.get(link + page)
        for class_name in self.req_input_class_names:
            with self.subTest(class_name=class_name):
                self.browser.find_element(By.CSS_SELECTOR, f'div.first_block input.{class_name}').send_keys("test")
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn(self.result_text, welcome_text, f"Not found text: '{self.result_text}'")


if __name__ == "__main__":
    unittest.main()

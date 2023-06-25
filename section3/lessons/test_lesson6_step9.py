import pytest
import time
import math
from selenium.webdriver.common.by import By


link = "https://www.google.com/"


def test_language(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "img.lnXdpd")
    time.sleep(5)


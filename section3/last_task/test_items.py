import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_display_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)

    assert len(browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")) != 0, \
        '[Button "Add to basket" not found]'


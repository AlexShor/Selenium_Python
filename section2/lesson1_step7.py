import time
from selenium import webdriver  # webdriver это и есть набор команд для управления браузером
from selenium.webdriver.common.by import By  # импортируем класс By, который позволяет выбрать способ поиска элемента
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()  # Инициализируем драйвер браузера. Открытие окна браузера

try:
    browser.get(link)

    y = calc(browser.find_element(By.ID, 'treasure').get_attribute('valuex'))
    browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # people_radio = browser.find_element(By.ID, "robotsRule")
    # people_checked = people_radio.get_attribute("checked")
    # print("value of people radio: ", people_checked)
    # assert people_checked is not None, "People radio is not selected by default"
    # assert people_checked == "true", "People radio is not selected by default"

finally:
    time.sleep(5)
    browser.quit()  # После выполнения всех действий мы должны не забыть закрыть окно браузера

# не забываем оставить пустую строку в конце файла

import time
from selenium import webdriver  # webdriver это и есть набор команд для управления браузером
from selenium.webdriver.common.by import By  # импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.support.ui import Select
import math
import os

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()  # Инициализируем драйвер браузера. Открытие окна браузера

try:
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    browser.switch_to.alert.accept()
    y = calc(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
    time.sleep(5)
    browser.quit()  # После выполнения всех действий мы должны не забыть закрыть окно браузера

# не забываем оставить пустую строку в конце файла

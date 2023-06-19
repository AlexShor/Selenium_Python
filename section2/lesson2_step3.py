import time
from selenium import webdriver  # webdriver это и есть набор команд для управления браузером
from selenium.webdriver.common.by import By  # импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.support.ui import Select
import math


link = "https://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()  # Инициализируем драйвер браузера. Открытие окна браузера

try:
    browser.get(link)
    s = str(sum([int(browser.find_element(By.ID, f'num{i+1}').text) for i in range(2)]))
    Select(browser.find_element(By.TAG_NAME, 'select')).select_by_value(s)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()


finally:
    time.sleep(5)
    browser.quit()  # После выполнения всех действий мы должны не забыть закрыть окно браузера

# не забываем оставить пустую строку в конце файла

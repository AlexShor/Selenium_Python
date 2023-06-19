import time
from selenium import webdriver  # webdriver это и есть набор команд для управления браузером
from selenium.webdriver.common.by import By  # импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.support.ui import Select
import math
import os


link = "http://suninjuly.github.io/file_input.html"

txt_file = 'test.txt'
open(txt_file, 'a').close()  # создаём файл, если отсутствует
file_path = os.path.abspath(txt_file)

browser = webdriver.Chrome()  # Инициализируем драйвер браузера. Открытие окна браузера

try:
    browser.get(link)

    for element in browser.find_elements(By.CSS_SELECTOR, 'input[type="text"]'):
        element.send_keys('test')
    browser.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(5)
    browser.quit()  # После выполнения всех действий мы должны не забыть закрыть окно браузера
    os.remove(txt_file)  # удаляем файл
# не забываем оставить пустую строку в конце файла

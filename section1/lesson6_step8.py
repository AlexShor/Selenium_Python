import time
import math
from selenium import webdriver  # webdriver это и есть набор команд для управления браузером
from selenium.webdriver.common.by import By  # импортируем класс By, который позволяет выбрать способ поиска элемента

link = "http://suninjuly.github.io/find_xpath_form"

browser = webdriver.Chrome()  # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера

try:
    browser.get(link)

    browser.find_element(By.TAG_NAME, 'input').send_keys("Ivan")
    browser.find_element(By.NAME, 'last_name').send_keys("Petrov")
    browser.find_element(By.CLASS_NAME, 'city').send_keys("Smolensk")
    browser.find_element(By.ID, "country").send_keys("Russia")

    browser.find_element(By.XPATH, "//button[text()='Submit']").click()

finally:
    time.sleep(15)
    browser.quit()  # После выполнения всех действий мы должны не забыть закрыть окно браузера

# не забываем оставить пустую строку в конце файла

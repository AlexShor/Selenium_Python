import time
from selenium import webdriver  # webdriver это и есть набор команд для управления браузером
from selenium.webdriver.common.by import By  # импортируем класс By, который позволяет выбрать способ поиска элемента

link = "http://suninjuly.github.io/simple_form_find_task.html"

browser = webdriver.Chrome()  # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера

try:
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, 'city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()  # После выполнения всех действий мы должны не забыть закрыть окно браузера

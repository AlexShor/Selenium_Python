import time
from selenium import webdriver  # webdriver это и есть набор команд для управления браузером
from selenium.webdriver.common.by import By  # импортируем класс By, который позволяет выбрать способ поиска элемента

link = "http://suninjuly.github.io/registration1.html"

browser = webdriver.Chrome()  # Инициализируем драйвер браузера. Открытие окна браузера

try:
    browser.get(link)

    req_input_class_names = ['first', 'second', 'third']

    # for class_name in req_input_class_names:
    #     browser.find_element(By.CLASS_NAME, 'first_block'). \
    #         find_element(By.CLASS_NAME, class_name).send_keys("test")

    for class_name in req_input_class_names:
        browser.find_element(By.CSS_SELECTOR, f'div.first_block input.{class_name}').send_keys("test")

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(1)

    welcome_text = browser.find_element(By.TAG_NAME, "h1").text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()  # После выполнения всех действий мы должны не забыть закрыть окно браузера

# не забываем оставить пустую строку в конце файла

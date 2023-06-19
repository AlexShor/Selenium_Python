import time
from selenium import webdriver  # webdriver это и есть набор команд для управления браузером
from selenium.webdriver.common.by import By  # импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import pyperclip

link = "http://suninjuly.github.io/explicit_wait2.html"
prise = 100

browser = webdriver.Chrome()  # Инициализируем драйвер браузера. Открытие окна браузера
browser.implicitly_wait(5)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def get_number_alert():  # Получение числа из алерта
    alert = browser.switch_to.alert
    alert_text = alert.text
    number = alert_text[alert_text.index(':') + 2:]
    pyperclip.copy(number)
    print(number)
    alert.accept()


try:
    browser.get(link)
    wait = WebDriverWait(browser, 12)

    wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), f'${prise}'))
    browser.find_element(By.CSS_SELECTOR, "button.btn[id='book']").click()

    y = calc(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "button.btn[id='solve']").click()

    get_number_alert()

    # assert "successful" in message.text

# except Exception as e:
#     print('\033[91m' + str(e)[:str(e).index('\n')])

finally:
    browser.quit()  # После выполнения всех действий мы должны не забыть закрыть окно браузера

# не забываем оставить пустую строку в конце файла

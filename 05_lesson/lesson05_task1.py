import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Настройка драйвера Chrome
driver = webdriver.Chrome()

# Открываем страницу
driver.get("http://uitestingplayground.com/classattr")

# Ждем загрузки страницы
time.sleep(2)

blue_button = driver.find_element(
    By.XPATH,
    "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]"
)

# Кликаем на синюю кнопку
blue_button.click()

time.sleep(3)

# Обрабатываем всплывающее окно alert
alert = Alert(driver)
alert.accept()

time.sleep(3)

print("Тест успешно выполнен!")

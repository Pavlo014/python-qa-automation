from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# 1. Переходим на страницу
driver.get("http://uitestingplayground.com/textinput")

# 2. Указываем в поле ввода текст SkyPro
input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input_field.send_keys("SkyPro")

# 3. Нажимаем на синюю кнопку
blue_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
blue_button.click()

# 4. Получаем текст кнопки и выводим в консоль
button_text = blue_button.text
print(button_text)

# Закрываем браузер
driver.quit()

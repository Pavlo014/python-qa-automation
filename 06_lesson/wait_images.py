from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# 1. Переходим на страницу
url = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
driver.get(url)

# 2. Дожидаемся загрузки всех картинок (ждем пока текст станет "Done!")
wait = WebDriverWait(driver, 15)
text_element = wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#text"), "Done!")
)

# 3. Получаем значение атрибута src у 3-й картинки
third_image = driver.find_element(By.CSS_SELECTOR, "#award")
src_value = third_image.get_attribute("src")

# 4. Выводим значение в консоль
print(src_value)

driver.quit()

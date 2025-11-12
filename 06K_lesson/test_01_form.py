from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    # Запускаем браузер Edge
    driver = webdriver.Edge()

    # 1. Открываем страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # 2. Заполняем форму значениями
    driver.find_element(
        By.CSS_SELECTOR, "input[name='first-name']"
    ).send_keys("Иван")
    driver.find_element(
        By.CSS_SELECTOR, "input[name='last-name']"
    ).send_keys("Петров")
    driver.find_element(
        By.CSS_SELECTOR, "input[name='address']"
    ).send_keys("Ленина, 55-3")
    driver.find_element(
        By.CSS_SELECTOR, "input[name='e-mail']"
    ).send_keys("test@skypro.com")
    driver.find_element(
        By.CSS_SELECTOR, "input[name='phone']"
    ).send_keys("+7985899998787")
    # Zip code оставляем пустым
    driver.find_element(
        By.CSS_SELECTOR, "input[name='city']"
    ).send_keys("Москва")
    driver.find_element(
        By.CSS_SELECTOR, "input[name='country']"
    ).send_keys("Россия")
    driver.find_element(
        By.CSS_SELECTOR, "input[name='job-position']"
    ).send_keys("QA")
    driver.find_element(
        By.CSS_SELECTOR, "input[name='company']"
    ).send_keys("SkyPro")

    # 3. Нажимаем кнопку Submit
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Ждем загрузки новой страницы
    wait = WebDriverWait(driver, 10)

    # 4. Проверяем, что поле Zip code подсвечено красным
    zip_code_alert = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger"))
    )
    assert zip_code_alert.text == "N/A"

    # 5. Проверяем, что остальные поля подсвечены зеленым
    success_alerts = driver.find_elements(By.CSS_SELECTOR, ".alert-success")
    assert len(success_alerts) == 9  # Все заполненные поля

    # Закрываем браузер
    driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    # Запускаем браузер Edge
    driver = webdriver.Edge()

    # 1. Открываем страницу
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    driver.get(url)

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

    # 4. Проверяем, что поле Zip code подсвечено красным (по ID)
    zip_code_field = wait.until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )
    assert "alert-danger" in zip_code_field.get_attribute("class")

    # 5. Проверяем, что остальные поля подсвечены зеленым
    success_fields_ids = [
        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "country", "job-position", "company"
    ]

    for field_id in success_fields_ids:
        field = driver.find_element(By.ID, field_id)
        assert "alert-success" in field.get_attribute("class")

    # Закрываем браузер
    driver.quit()

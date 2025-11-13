from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    driver = webdriver.Chrome()

    # Открываем страницу калькулятора
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    driver.get(url)

    # Ожидаем загрузки страницы
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "delay"))
    )

    # Очищаем поле ввода задержки и вводим значение 45
    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажимаем кнопки: 7 + 8 =
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # Ожидаем появления результата в течение 45 секунд
    WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )

    # Проверяем, что результат равен 15
    result = driver.find_element(By.CLASS_NAME, "screen").text
    assert result == "15", f"Ожидался результат 15, но получили {result}"

    print("Тест успешно пройден! Результат: 15")

    driver.quit()


if __name__ == "__main__":
    test_slow_calculator()

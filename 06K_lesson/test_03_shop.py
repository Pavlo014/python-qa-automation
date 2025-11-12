from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_purchase():
    # Настройки для Firefox
    firefox_options = Options()
    firefox_options.add_argument("--width=1920")
    firefox_options.add_argument("--height=1080")

    driver = webdriver.Firefox(options=firefox_options)

    driver.get("https://www.saucedemo.com/")

    # Ожидаем загрузки страницы
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )

    # Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Ожидаем загрузки главной страницы после авторизации
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    # Добавляем товары в корзину
    products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for product in products:
        xpath_locator = (
            f"//div[text()='{product}']"
            "/ancestor::div[@class='inventory_item']//button"
        )
        add_to_cart_button = driver.find_element(By.XPATH, xpath_locator)
        add_to_cart_button.click()

    # Переходим в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Ожидаем загрузки корзины
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "checkout"))
    )

    # Нажимаем Checkout
    driver.find_element(By.ID, "checkout").click()

    # Ожидаем загрузки формы
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )

    # Заполняем форму
    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Иванов")
    driver.find_element(By.ID, "postal-code").send_keys("455000")

    # Нажимаем Continue
    driver.find_element(By.ID, "continue").click()

    # Ожидаем загрузки страницы с итогами
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )

    # Читаем итоговую стоимость
    total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
    total_text = total_element.text
    total_amount = total_text.replace("Total: $", "")

    # Проверяем итоговую сумму
    assert total_amount == "58.29", (
        f"Ожидалась сумма $58.29, но получили ${total_amount}"
    )

    print(f"Тест успешно пройден! Итоговая сумма: ${total_amount}")

    driver.quit()


if __name__ == "__main__":
    test_purchase()

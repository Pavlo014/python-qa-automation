import pytest
import allure
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture()
def driver():
    """Фикстура для инициализации драйвера."""
    driver_instance = webdriver.Chrome()
    driver_instance.maximize_window()
    driver_instance.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )
    yield driver_instance
    driver_instance.quit()


@allure.feature("Калькулятор")
@allure.severity("critical")
@allure.title("Проверка работы медленного калькулятора")
@allure.description("Тест проверяет вычисление 7 + 8 с задержкой 45 секунд")
def test_slow_calculator(driver):
    calculator_page = CalculatorPage(driver)

    with allure.step("Установить задержку 45 секунд"):
        calculator_page.set_delay(45)

    with allure.step("Ввести выражение 7 + 8"):
        calculator_page.click_button("7")
        calculator_page.click_button("+")
        calculator_page.click_button("8")

    with allure.step("Нажать кнопку 'равно'"):
        calculator_page.click_button("=")

    with allure.step("Получить результат вычислений"):
        result = calculator_page.get_result()

    with allure.step("Проверить, что результат равен 15"):
        assert result == "15", f"Ожидался результат 15, но получили {result}"

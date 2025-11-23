import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture()
def driver():
    driver_instance = webdriver.Chrome()
    driver_instance.maximize_window()
    driver_instance.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )
    yield driver_instance
    driver_instance.quit()


def test_slow_calculator(driver):
    calculator_page = CalculatorPage(driver)

    calculator_page.perform_calculation(45, "7", "+", "8", "=")

    result = calculator_page.get_result()

    assert result == "15", f"Ожидался результат 15, но получили {result}"
    print(f"Тест успешно пройден! Результат: {result}")

import pytest
import allure
from selenium import webdriver
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture()
def driver():
    """Фикстура для инициализации драйвера."""
    driver_instance = webdriver.Firefox()
    driver_instance.maximize_window()
    yield driver_instance
    driver_instance.quit()


@allure.feature("Магазин")
@allure.severity("critical")
@allure.title("Проверка полного цикла покупки товаров")
@allure.description("Тест проверяет авторизацию, добавление товаров, "
                    "оформление заказа и проверку итоговой суммы")
def test_purchase_flow(driver):
    with allure.step("Авторизация пользователя"):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавление товаров в корзину"):
        main_page = MainPage(driver)
        main_page.wait_for_load()

        products = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]

        for product in products:
            with allure.step(f"Добавить товар '{product}' в корзину"):
                main_page.add_product_to_cart(product)

    with allure.step("Переход в корзину"):
        main_page.go_to_cart()

    with allure.step("Оформление заказа"):
        cart_page = CartPage(driver)
        cart_page.wait_for_load()
        cart_page.proceed_to_checkout()

    with allure.step("Заполнение формы оформления заказа"):
        checkout_page = CheckoutPage(driver)
        checkout_page.wait_for_load()
        checkout_page.fill_checkout_form("Иван", "Иванов", "450450")
        checkout_page.continue_to_overview()

    with allure.step("Получение итоговой суммы заказа"):
        total_amount = checkout_page.get_total_amount()

    with allure.step("Проверка итоговой суммы"):
        assert total_amount == "58.29", (
            f"Ожидалась сумма $58.29, но получили ${total_amount}"
        )

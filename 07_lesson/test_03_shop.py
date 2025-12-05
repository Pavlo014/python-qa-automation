import pytest
from selenium import webdriver
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture()
def driver():
    driver_instance = webdriver.Firefox()
    driver_instance.maximize_window()
    yield driver_instance
    driver_instance.quit()


def test_purchase_flow(driver):
    # Шаг 1: Авторизация
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Шаг 2: Добавление товаров в корзину
    main_page = MainPage(driver)
    main_page.wait_for_load()

    products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for product in products:
        main_page.add_product_to_cart(product)

    # Шаг 3: Переход в корзину
    main_page.go_to_cart()

    # Шаг 4: Оформление заказа
    cart_page = CartPage(driver)
    cart_page.wait_for_load()
    cart_page.proceed_to_checkout()

    # Шаг 5: Заполнение формы
    checkout_page = CheckoutPage(driver)
    checkout_page.wait_for_load()
    checkout_page.fill_checkout_form("Иван", "Иванов", "450450")
    checkout_page.continue_to_overview()

    # Шаг 6: Проверка итоговой суммы
    total_amount = checkout_page.get_total_amount()

    # Проверка
    assert total_amount == "58.29", (
        f"Ожидалась сумма $58.29, но получили ${total_amount}"
    )

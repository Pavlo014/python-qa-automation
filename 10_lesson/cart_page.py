from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """Класс для работы со страницей корзины."""

    def __init__(self, driver):
        """
        Инициализация страницы корзины.

        :param driver: WebDriver экземпляр.
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    def wait_for_load(self) -> None:
        """Ожидание загрузки страницы корзины."""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.checkout_button)
        )

    def proceed_to_checkout(self) -> None:
        """Переход к оформлению заказа."""
        self.driver.find_element(*self.checkout_button).click()

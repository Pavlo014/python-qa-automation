from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """Класс для работы со страницей оформления заказа."""

    def __init__(self, driver):
        """
        Инициализация страницы оформления заказа.

        :param driver: WebDriver экземпляр.
        """
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def wait_for_load(self) -> None:
        """Ожидание загрузки страницы оформления заказа."""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.first_name_field)
        )

    def fill_checkout_form(
        self,
        first_name: str,
        last_name: str,
        postal_code: str
    ) -> None:
        """
        Заполнение формы данными покупателя.

        :param first_name: Имя покупателя.
        :param last_name: Фамилия покупателя.
        :param postal_code: Почтовый индекс.
        """
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        postal_field = self.driver.find_element(*self.postal_code_field)
        postal_field.send_keys(postal_code)

    def continue_to_overview(self) -> None:
        """Переход к странице обзора заказа."""
        self.driver.find_element(*self.continue_button).click()

    def get_total_amount(self) -> str:
        """
        Получение итоговой суммы заказа.

        :return: Итоговая сумма без символа валюты.
        """
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.total_label)
        )
        total_element = self.driver.find_element(*self.total_label)
        total_text = total_element.text
        return total_text.replace("Total: $", "")

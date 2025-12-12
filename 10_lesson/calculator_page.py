from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Класс для работы со страницей калькулятора."""

    def __init__(self, driver):
        """
        Инициализация страницы калькулятора.

        :param driver: WebDriver экземпляр.
        """
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.screen = (By.CLASS_NAME, "screen")
        self.button_locator = "//span[text()='{}']"

    def set_delay(self, delay_value: int) -> None:
        """
        Установка задержки вычислений.

        :param delay_value: Значение задержки в секундах.
        """
        delay_element = self.driver.find_element(*self.delay_input)
        delay_element.clear()
        delay_element.send_keys(str(delay_value))

    def click_button(self, button: str) -> None:
        """
        Нажатие кнопки на калькуляторе.

        :param button: Текст на кнопке (например, '7', '+', '=').
        """
        locator = (By.XPATH, self.button_locator.format(button))
        button_element = self.driver.find_element(*locator)
        button_element.click()

    def get_result(self, timeout: int = 50) -> str:
        """
        Получение результата вычислений.

        :param timeout: Максимальное время ожидания.
        :return: Текст результата на экране калькулятора.
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.screen, "15")
        )
        result_element = self.driver.find_element(*self.screen)
        return result_element.text

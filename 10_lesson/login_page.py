from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Класс для работы со страницей авторизации."""

    def __init__(self, driver):
        """
        Инициализация страницы авторизации.

        :param driver: WebDriver экземпляр.
        """
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self) -> None:
        """Открытие страницы авторизации."""
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_field)
        )

    def login(self, username: str, password: str) -> None:
        """
        Выполнение авторизации.

        :param username: Логин пользователя.
        :param password: Пароль пользователя.
        """
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

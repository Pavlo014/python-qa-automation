from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.screen = (By.CLASS_NAME, "screen")
        self.buttons = {
            "0": (By.XPATH, "//span[text()='0']"),
            "1": (By.XPATH, "//span[text()='1']"),
            "2": (By.XPATH, "//span[text()='2']"),
            "3": (By.XPATH, "//span[text()='3']"),
            "4": (By.XPATH, "//span[text()='4']"),
            "5": (By.XPATH, "//span[text()='5']"),
            "6": (By.XPATH, "//span[text()='6']"),
            "7": (By.XPATH, "//span[text()='7']"),
            "8": (By.XPATH, "//span[text()='8']"),
            "9": (By.XPATH, "//span[text()='9']"),
            "+": (By.XPATH, "//span[text()='+']"),
            "-": (By.XPATH, "//span[text()='-']"),
            "×": (By.XPATH, "//span[text()='x']"),
            "÷": (By.XPATH, "//span[text()='÷']"),
            "=": (By.XPATH, "//span[text()='=']"),
            ".": (By.XPATH, "//span[text()='.']"),
            "C": (By.CLASS_NAME, "clear")
        }

    def set_delay(self, delay_value):
        delay_element = self.driver.find_element(*self.delay_input)
        delay_element.clear()
        delay_element.send_keys(str(delay_value))

    def click_button(self, button):
        button_element = self.driver.find_element(*self.buttons[button])
        button_element.click()

    def get_result(self, timeout=50):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.screen, "15")
        )
        result_element = self.driver.find_element(*self.screen)
        return result_element.text

    def perform_calculation(self, delay, *buttons):
        self.set_delay(delay)
        for button in buttons:
            self.click_button(button)

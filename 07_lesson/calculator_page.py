from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.screen = (By.CLASS_NAME, "screen")
        self.button_locator = "//span[text()='{}']"

    def set_delay(self, delay_value):
        delay_element = self.driver.find_element(*self.delay_input)
        delay_element.clear()
        delay_element.send_keys(str(delay_value))

    def click_button(self, button):
        locator = (By.XPATH, self.button_locator.format(button))
        button_element = self.driver.find_element(*locator)
        button_element.click()

    def get_result(self, timeout=50):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.screen, "15")
        )
        result_element = self.driver.find_element(*self.screen)
        return result_element.text

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")
        self.inventory_list = (By.CLASS_NAME, "inventory_list")

    def wait_for_load(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.inventory_list)
        )

    def add_product_to_cart(self, product_name):
        xpath_locator = (
            f"//div[text()='{product_name}']"
            "/ancestor::div[@class='inventory_item']//button"
        )
        add_button = self.driver.find_element(By.XPATH, xpath_locator)
        add_button.click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()

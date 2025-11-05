from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")

time.sleep(3)

button = driver.find_element(
    By.XPATH,
    "//button[contains(text(), 'Button with Dynamic ID')]"
)

button.click()

time.sleep(3)

driver.quit()

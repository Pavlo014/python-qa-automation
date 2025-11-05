from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
time.sleep(3)

driver.get("http://the-internet.herokuapp.com/login")
time.sleep(3)

username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")
time.sleep(3)

password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")
time.sleep(3)

login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
login_button.click()
time.sleep(3)

flash_message = driver.find_element(By.ID, "flash")
print(flash_message.text)
time.sleep(3)

driver.quit()
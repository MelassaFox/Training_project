import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

base_url = 'https://www.saucedemo.com/'
login_first = 'standard_use'
password_all = 'secret_sauce'

driver.get(base_url)
driver.fullscreen_window()

username = driver.find_element(By.XPATH, value='//*[@id="user-name"]')  # FullXPATH
username.send_keys(login_first)

password = driver.find_element(By.CSS_SELECTOR, value='#password')  #CSS_SELECTOR
password.send_keys(password_all)

login_button = driver.find_element(By.XPATH, value='//*[@id="login-button"]')
login_button.click()

warning_text = driver.find_element(By.XPATH, value='//*[@id="login_button_container"]/div/form/div[3]/h3')
value_warning_test = warning_text.text
assert value_warning_test == 'Epic sadface: Username and password do not match any user in this service'

driver.refresh()
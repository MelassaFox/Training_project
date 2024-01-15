from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    driver = webdriver.Chrome()

    base_url = 'https://www.saucedemo.com/'
    login_first = 'standard_user'
    password_all = 'secret_sauce'

    driver.get(base_url)
    driver.fullscreen_window()

    username = driver.find_element(By.XPATH, value='//*[@id="user-name"]')  # FullXPATH
    username.send_keys(login_first)

    username.clear()

finally:
    driver.quit()

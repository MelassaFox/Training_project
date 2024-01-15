from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')
    driver.fullscreen_window()

    username = driver.find_element(By.XPATH, value='//*[@id="user-name"]')  # FullXPATH
    username.send_keys('standard_user')

    password = driver.find_element(By.CSS_SELECTOR, value='#password') #CSS_SELECTOR
    password.send_keys('secret_sauce')

    login_button = driver.find_element(By.XPATH, value='//*[@id="login-button"]')
    login_button.click()

finally:
    driver.quit()

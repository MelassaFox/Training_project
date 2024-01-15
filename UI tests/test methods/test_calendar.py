import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
try:
    driver = webdriver.Chrome()

    base_url = 'https://www.lambdatest.com/selenium-playground/jquery-date-picker-demo'

    driver.get(base_url)
    driver.fullscreen_window()

    new_day = driver.find_element(By.XPATH, value="//input[@id='from']")
    new_day.clear()

    new_day.send_keys('01/10/2024')
    new_day.send_keys(Keys.RETURN)
    time.sleep(2)

finally:
    driver.quit()

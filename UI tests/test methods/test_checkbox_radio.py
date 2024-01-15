import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    driver = webdriver.Chrome()

    base_url = 'https://testpages.herokuapp.com/styled/basic-html-form-test.html'

    driver.get(base_url)
    driver.fullscreen_window()
    checkbox = driver.find_element(By.XPATH, value="//input[@value='cb1']")
    checkbox.click()
    checkbox = driver.find_element(By.XPATH, value="//input[@value='cb3']")
    checkbox.click()

    radiobatton = driver.find_element(By.XPATH, value="//input[@value='rd1']")
    radiobatton.click()
    time.sleep(2)

finally:
    driver.quit()

import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    driver = webdriver.Chrome()

    base_url = 'https://demoqa.com/dynamic-properties'
    new_url = 'https://demoqa.com/radio-button'
    driver.get(base_url)
    driver.fullscreen_window()

    try:
        visible_button = driver.find_element(By.XPATH, value='//*[@id="visibleAfter"]')
        visible_button.click()

    except NoSuchElementException as exception:
        time.sleep(10)
        visible_button = driver.find_element(By.XPATH, value='//*[@id="visibleAfter"]')
        visible_button.click()

finally:
    driver.quit()

import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    driver = webdriver.Chrome()

    base_url = 'https://demoqa.com/radio-button'
    driver.get(base_url)
    driver.fullscreen_window()

    yes_button = driver.find_element(By.XPATH, value="//label[@for='yesRadio']")
    yes_button.click()
    try:
        message = driver.find_element(By.XPATH, value="//span[@class='text-success']")
        value_message = message.text
        assert value_message == 'No'
    except AssertionError as exception:
        driver.refresh()
        yes_button = driver.find_element(By.XPATH, value="//label[@for='yesRadio']")
        yes_button.click()
        message = driver.find_element(By.XPATH, value="//span[@class='text-success']")
        value_message = message.text
        assert value_message == 'Yes'

    print('Test over')

finally:
    driver.quit()

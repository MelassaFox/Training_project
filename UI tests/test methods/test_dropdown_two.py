import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

try:
    driver = webdriver.Chrome()

    base_url = 'https://www.lambdatest.com/selenium-playground/jquery-dropdown-search-demo'

    driver.get(base_url)
    driver.fullscreen_window()

    click_dropdown = driver.find_element(By.XPATH, value='//span[@aria-labelledby="select2-country-container"]')
    click_dropdown.click()

    select_country = driver.find_element(By.XPATH, value='(//li[@class="select2-results__option"])[4]')
    select_country.click()

    time.sleep(3)

    click_dropdown = driver.find_element(By.XPATH, value='//span[@aria-labelledby="select2-country-container"]')
    click_dropdown.click()

    input_country = driver.find_element(By.XPATH, value='(//input[@class="select2-search__field"])[2]')
    input_country.send_keys('India')
    input_country.send_keys(Keys.RETURN)

    time.sleep(3)

finally:
    driver.quit()

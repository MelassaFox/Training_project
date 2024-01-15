import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

try:
    driver = webdriver.Chrome()

    base_url = 'https://www.saucedemo.com/'
    login_first = 'standard_user'
    password_all = 'secret_sauce'

    driver.get(base_url)
    driver.fullscreen_window()

    username = driver.find_element(By.XPATH, value='//*[@id="user-name"]')  # FullXPATH
    username.send_keys(login_first)

    password = driver.find_element(By.CSS_SELECTOR, value='#password')  #CSS_SELECTOR
    password.send_keys(password_all)

    login_button = driver.find_element(By.XPATH, value='//*[@id="login-button"]')
    login_button.click()

    select = Select(driver.find_element(By.XPATH, value='//select[@class="product_sort_container"]'))
    #select.select_by_visible_text('Name (Z to A)')

    select.select_by_value('hilo')
    time.sleep(2)

finally:
    driver.quit()

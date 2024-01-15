import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    driver = webdriver.Chrome()

    base_url = 'https://www.saucedemo.com/'
    login_first = 'standard_user'
    password_all = 'secret_sauce'

    driver.get(base_url)
    driver.fullscreen_window()

    username = driver.find_element(By.XPATH, value='//*[@id="user-name"]')  # FullXPATH
    username.send_keys(login_first)
    username.send_keys(Keys.BACKSPACE)      # стирает последний символ
    username.send_keys('r')

    password = driver.find_element(By.CSS_SELECTOR, value='#password')  # CSS_SELECTOR
    password.send_keys(password_all)
    password.send_keys(Keys.RETURN)     # Нажатие кнопки ENTER

    filter = driver.find_element(By.XPATH, value='//select[@data-test="product_sort_container"]')
    filter.click()
    select = Select(filter)
    select.select_by_index(1)
    time.sleep(3)

finally:
    driver.quit()

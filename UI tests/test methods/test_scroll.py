import time

from selenium import webdriver
from selenium.webdriver import ActionChains
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

    password = driver.find_element(By.CSS_SELECTOR, value='#password')  #CSS_SELECTOR
    password.send_keys(password_all)

    login_button = driver.find_element(By.XPATH, value='//*[@id="login-button"]')
    login_button.click()

    #driver.execute_script('window.scrollTo(0, 900)')

    action = ActionChains(driver)
    red_t_shit = driver.find_element(By.XPATH, value='//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
    action.move_to_element(red_t_shit).perform()


    time.sleep(2)

finally:
    driver.quit()

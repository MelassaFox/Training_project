import time

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

    password = driver.find_element(By.CSS_SELECTOR, value='#password')  #CSS_SELECTOR
    password.send_keys(password_all)

    login_button = driver.find_element(By.XPATH, value='//*[@id="login-button"]')
    login_button.click()

    url = 'https://www.saucedemo.com/inventory.html'
    get_url = driver.current_url
    assert url == get_url

    menu = driver.find_element(By.XPATH, value='//*[@id="react-burger-menu-btn"]')
    menu.click()

    time.sleep(2)

    link_about = driver.find_element(By.XPATH, value='//a[@id="about_sidebar_link"]')
    link_about.click()

    driver.back()   # переход назад
    time.sleep(2)

    driver.forward()    # переход вперед
    time.sleep(2)
    

finally:
    driver.quit()

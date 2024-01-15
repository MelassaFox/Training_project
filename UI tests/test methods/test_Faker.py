import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker

try:
    driver = webdriver.Chrome()
    base_url = 'https://www.saucedemo.com/'
    driver.get(base_url)
    driver.fullscreen_window()

    faker = Faker('en_US')

    name = faker.first_name() + str(faker.random_int())
    password = faker.password()

    username = driver.find_element(By.XPATH, value='//*[@id="user-name"]')  # FullXPATH
    username.send_keys(name)
    user_password = driver.find_element(By.CSS_SELECTOR, value='#password')  # CSS_SELECTOR
    user_password.send_keys(password)

    time.sleep(3)

finally:
    driver.quit()

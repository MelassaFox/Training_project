import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Test_1():
    def test_select_product(self):
        driver = webdriver.Chrome()
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()

        name_user = "standard_user"
        password_user = "secret_sauce"

        user_name = WebDriverWait(driver, timeout=30).until(EC.element_to_be_clickable
                                                             ((By.XPATH, '//*[@id="user-name"]')))
        user_name.send_keys(name_user)
        print('Input Login')

        password = WebDriverWait(driver, timeout=30).until(EC.element_to_be_clickable
                                                             ((By.XPATH, '//*[@id="password"]')))
        password.send_keys(password_user)
        print('Input Password')

        button_login = WebDriverWait(driver, timeout=30).until(EC.element_to_be_clickable
                                                             ((By.XPATH, '//*[@id="login-button"]')))
        button_login.click()
        print('Click Login Button')

        select_product = WebDriverWait(driver, timeout=30).until(EC.element_to_be_clickable
                                                             ((By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')))
        select_product.click()
        print('Click Select Product')

        enter_basket = WebDriverWait(driver, timeout=30).until(EC.element_to_be_clickable
                                                                 ((By.XPATH,
                                                                   '//*[@id="shopping_cart_container"]')))
        enter_basket.click()
        print('Click Enter Shopping Cart')

        success_test = WebDriverWait(driver, timeout=30).until(EC.element_to_be_clickable
                                                                 ((By.XPATH, '//span[@class="title"]')))
        value_success_test = success_test.text
        assert value_success_test == 'Your Cart'
        print('Checking successful transfer to cart')

test = Test_1()
test.test_select_product()

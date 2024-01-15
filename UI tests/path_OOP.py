import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

logging.basicConfig(level=logging.INFO)

class Test_1():
  def __init__(self):
      self.driver = webdriver.Chrome()
      self.driver.fullscreen_window()

  def input_data(self, xpath, value):
      try:
          element = WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH, xpath)))
          element.send_keys(value)
          logging.info(f'Input {value}')
      except Exception as e:
          logging.error(f'An error occurred: {str(e)}')

  def click_element(self, xpath):
      try:
          element = WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH, xpath)))
          element.click()
          logging.info(f'Click {xpath}')
      except Exception as e:
          logging.error(f'An error occurred: {str(e)}')

  def test_select_product(self):
      base_url = 'https://www.saucedemo.com/'
      self.driver.get(base_url)

      self.input_data(xpath='//*[@id="user-name"]', value="standard_user")
      self.input_data(xpath='//*[@id="password"]', value="secret_sauce")
      self.click_element('//*[@id="login-button"]')
      self.click_element('//*[@id="add-to-cart-sauce-labs-backpack"]')
      self.click_element('//*[@id="shopping_cart_container"]')

      success_test = WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH, '//span[@class="title"]')))
      value_success_test = success_test.text
      assert value_success_test == 'Your Cart'
      logging.info('Checking successful transfer to cart')

  def close(self):
      self.driver.quit()

test = Test_1()
test.test_select_product()
test.close()

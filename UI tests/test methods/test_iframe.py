import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

try:
    driver = webdriver.Chrome()
    base_url = 'https://www.lambdatest.com/selenium-playground/iframe-demo/'

    driver.get(base_url)
    driver.fullscreen_window()

    iframe = driver.find_element(By.XPATH, value="//iframe[@id='iFrame1']")
    driver.switch_to.frame(iframe)

    input_text = driver.find_element(By.XPATH, value="//div[@id='__next']/div/div[2]")
    value_input_text = input_text.text

    input_text.send_keys(Keys.COMMAND + 'a')

    click_editing_panel = driver.find_element(By.XPATH, value="//button[@title='Bold']")
    click_editing_panel.click()

    bold_text = driver.find_element(By.XPATH, value="//div[@id='__next']/div/div[2]/b")
    value_bold_text = bold_text.text

    assert value_input_text == value_bold_text

    time.sleep(3)

finally:
    driver.quit()

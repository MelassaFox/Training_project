import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

try:
    driver = webdriver.Chrome()
    base_url = 'https://www.lambdatest.com/selenium-playground/simple-form-demo'

    driver.get(base_url)
    driver.fullscreen_window()

    message = 'Hello'

    input_text = driver.find_element(By.XPATH, value='//input[@id="user-message"]')
    input_text.send_keys(message)

    input_button = driver.find_element(By.XPATH, value='//button[@id="showInput"]')
    input_button.click()

    message_wr = driver.find_element(By.XPATH, value='//p[@id="message"]')
    value_message = message_wr.text
    assert value_message == message

    input_message_first = 123
    input_message_second = 234
    summ = input_message_first + input_message_second

    input_text_first = driver.find_element(By.XPATH, value='//input[@id="sum1"]')
    input_text_first.send_keys(input_message_first)

    input_text_second = driver.find_element(By.XPATH, value='//input[@id="sum2"]')
    input_text_second.send_keys(input_message_second)

    sum_button = driver.find_element(By.XPATH, value="//button[contains(text(), 'Get Sum')]")
    sum_button.click()

    sum_wr = driver.find_element(By.XPATH, value='//p[@id="addmessage"]')
    value_sum = sum_wr.text
    assert value_sum == str(summ)

    time.sleep(2)

finally:
    driver.quit()

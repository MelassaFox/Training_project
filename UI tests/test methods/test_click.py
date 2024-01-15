import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

try:
    driver = webdriver.Chrome()

    base_url = 'https://demoqa.com/buttons'

    driver.get(base_url)
    driver.fullscreen_window()
    time.sleep(2)

    action = ActionChains(driver)

    double_clik = driver.find_element(By.XPATH, value="//button[@id='doubleClickBtn']")
    action.double_click(double_clik).perform()  # сохраняет результат действия

    right_click = driver.find_element(By.XPATH, value="//button[@id='rightClickBtn']")
    action.context_click(right_click).perform()

finally:
    driver.quit()

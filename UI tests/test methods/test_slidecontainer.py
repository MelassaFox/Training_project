import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

try:
    driver = webdriver.Chrome()

    base_url = 'https://www.schoolsw3.com/howto/howto_js_rangeslider.php'

    driver.get(base_url)
    driver.fullscreen_window()

    action = ActionChains(driver)   # управление мышью
    price = driver.find_element(By.XPATH, value='//input[@id="id3"]')
    action.click_and_hold(price).move_by_offset(xoffset=200, yoffset=0).release().perform()

    time.sleep(5)

finally:
    driver.quit()

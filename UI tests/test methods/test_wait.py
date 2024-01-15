
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

try:
    driver = webdriver.Chrome()

    base_url = 'https://demoqa.com/dynamic-properties'
    driver.get(base_url)

    # driver.implicitly_wait(10)   #задача неявного времени ожидания
    # visible_button = driver.find_element(By.XPATH, value='//*[@id="visibleAfter"]')

    visible_button = WebDriverWait(driver, timeout=30).until(EC.element_to_be_clickable
                                                             ((By.XPATH, '//*[@id="visibleAfter"]')))     #явное время ожидания
    visible_button.click()

finally:
    driver.quit()

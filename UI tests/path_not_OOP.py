from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
driver.maximize_window()

name_user = "standard_user"
password_user = "secret_sauce"
info_product = ""
info_product_cost = ""
product_basket = ""

'''Authorisation'''

user_name = driver.find_element(By.XPATH, value='//*[@id="user-name"]')  # ввод логина для авторизации
user_name.send_keys(name_user)

password = driver.find_element(By.CSS_SELECTOR, value='#password')  # ввод пароля для авторизации
password.send_keys(password_user)

button_login = driver.find_element(By.XPATH, value='//*[@id="login-button"]')  # поиск кнопки авторизации
button_login.click()

'''Product choice'''

print('Привет, друг!\nРады приветствовать тебя в магазине!\nКакой товар тебя интересует?')
print('1 - Sauce Labs Backpack\n2 - Sauce Labs Bike Light\n3 - Sauce Labs Bolt T-Shirt'
      '\n4 - Sauce Labs Fleece Jacket\n5 - Sauce Labs Onesie\n6 - Test.allTheThings() T-Shirt (Red)')
product = input('Введи номер товара: ')
product_number = int(product)

if product_number == 1:

    product = driver.find_element(By.CSS_SELECTOR, value='#item_4_title_link')  # название первого товара
    info_product = product.text

    product_cost = driver.find_element(By.XPATH, value='//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')  # цена первого товара
    info_product_cost = product_cost.text

    product_button = driver.find_element(By.XPATH, value='//*[@id="add-to-cart-sauce-labs-backpack"]')  # добавление в корзину первого товара
    product_button.click()

elif product_number == 2:

    product = driver.find_element(By.CSS_SELECTOR, value='#item_0_title_link')  # название второго товара
    info_product = product.text

    product_cost = driver.find_element(By.XPATH, value='//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div')  # цена второго товара
    info_product_cost = product_cost.text

    product_button = driver.find_element(By.XPATH, value='//*[@id="add-to-cart-sauce-labs-bike-light"]')  # добавление в корзину второго товара
    product_button.click()

elif product_number == 3:

    product = driver.find_element(By.CSS_SELECTOR, value='#item_1_title_link')  # название третьего товара
    info_product = product.text

    product_cost = driver.find_element(By.XPATH, value='//*[@id="inventory_container"]/div/div[3]/div[2]/div[2]/div')  # цена третьего товара
    info_product_cost = product_cost.text

    product_button = driver.find_element(By.XPATH, value='//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')  # добавление в корзину третьего товара
    product_button.click()

elif product_number == 4:

    product = driver.find_element(By.CSS_SELECTOR, value='#item_5_title_link')  # название четвертого товара
    info_product = product.text

    product_cost = driver.find_element(By.XPATH, value='//*[@id="inventory_container"]/div/div[4]/div[2]/div[2]/div')  # цена четвертого товара
    info_product_cost = product_cost.text

    product_button = driver.find_element(By.XPATH, value='//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')  # добавление в корзину четвертого товара
    product_button.click()

elif product_number == 5:

    product = driver.find_element(By.CSS_SELECTOR, value='#item_2_title_link')  # название пятого товара
    info_product = product.text

    product_cost = driver.find_element(By.XPATH, value='//*[@id="inventory_container"]/div/div[3]/div[2]/div[2]/div')  # цена пятого товара
    info_product_cost = product_cost.text

    product_button = driver.find_element(By.XPATH, value='//*[@id="add-to-cart-sauce-labs-onesie"]')  # добавление в корзину пятого товара
    product_button.click()

elif product_number == 6:

    product = driver.find_element(By.CSS_SELECTOR, value='#item_3_title_link')  # название шестого товара
    info_product = product.text

    product_cost = driver.find_element(By.XPATH, value='//*[@id="inventory_container"]/div/div[6]/div[2]/div[2]/div')  # цена шестого товара
    info_product_cost = product_cost.text

    product_button = driver.find_element(By.XPATH, value='//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')  # добавление в корзину шестого товара
    product_button.click()

else:
    print('Такого товара нет в нашем каталоге')

'''Work to basket'''

basket_button = driver.find_element(By.XPATH, value='//*[@id="shopping_cart_container"]/a')  # переход в корзину
basket_button.click()

if product_number == 1:

    product_basket = driver.find_element(By.CSS_SELECTOR, value='#item_4_title_link')  # название первого товара
    product_basket = product_basket.text

elif product_number == 2:

    product_basket = driver.find_element(By.CSS_SELECTOR, value='#item_0_title_link')  # название второго товара
    product_basket = product_basket.text

elif product_number == 3:

    product_basket = driver.find_element(By.CSS_SELECTOR, value='#item_1_title_link')  # название третьего товара
    product_basket = product_basket.text

elif product_number == 4:

    product_basket = driver.find_element(By.CSS_SELECTOR, value='#item_5_title_link')  # название четвертого товара
    product_basket = product_basket.text

elif product_number == 5:

    product_basket = driver.find_element(By.CSS_SELECTOR, value='#item_2_title_link')  # название пятого товара
    product_basket = product_basket.text

elif product_number == 6:

    product_basket = driver.find_element(By.CSS_SELECTOR, value='#item_3_title_link')  # название шестого товара
    product_basket = product_basket.text

assert info_product == product_basket  # сравнение названия продукта на главной странице и в корзине
print('Name product correctly')

product_cost_basket = driver.find_element(By.CSS_SELECTOR, value='#cart_contents_container > div > div.cart_list > div.cart_item > '
                                                           'div.cart_item_label > div.item_pricebar > div')  # цена первого товара
product_cost_basket = product_cost_basket.text

assert info_product_cost == product_cost_basket  # сравнение цены продукта на главной странице и в корзине
print('Cost product correctly')

'''Work to chekout'''

checkout_button = driver.find_element(By.XPATH, value='//*[@id="checkout"]')  # переход к оформлению заказа
checkout_button.click()

first_name_order = driver.find_element(By.XPATH, value='//*[@id="first-name"]')  # ввод имени
first_name_order.send_keys(name_user)

second_name_order = driver.find_element(By.XPATH, value='//*[@id="last-name"]')  # ввод фамилии
second_name_order.send_keys(name_user)

postal_code = driver.find_element(By.XPATH, value='//*[@id="postal-code"]')  # ввод почтового кода
postal_code.send_keys(password_user)

continue_button = driver.find_element(By.XPATH, value='//*[@id="continue"]')  # клик по кнопке далее
continue_button.click()

'''Work to cost products'''
cost_basket_first_product = float(product_cost_basket[1:])  # преобразование стоимости товара в число

total_cost_basket = driver.find_element(By.CSS_SELECTOR, value='#checkout_summary_container > div > '
                                                         'div.summary_info > div.summary_subtotal_label')  # достаем общую стоимость
info_total_cost_basket = total_cost_basket.text
delete_text = 'Item total: $'
total_cost_basket_float = float(info_total_cost_basket.lstrip(delete_text))  # преобразование общей стоимости к числу

if total_cost_basket_float == cost_basket_first_product:
    print('Total cost correctly')
else:
    print('Total cost NO correctly')

'''Finish him!'''

finish_button = driver.find_element(By.XPATH, value='//*[@id="finish"]')  # клик по кнопке финиш
finish_button.click()

print('Congratulations! The test worked correctly')
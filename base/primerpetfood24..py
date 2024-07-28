import time
import re
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument("--headless")
g = Service()
driver = webdriver.Chrome(options=options, service=g)
driver.get('https://petfood24.ru/')
driver.maximize_window()

actions = ActionChains(driver)

"""Переход с главной страницы в cat_page"""
cats = driver.find_element(By.XPATH, "(//span[contains(text(), 'Кошки')])[1]")
cats.click()
print("успешно")


"""Переход с cat_page в corm_page"""
driver.execute_script("window.scrollTo(0, 300);")
corm = driver.find_element(By.XPATH, "(//a[contains(text(), 'Сухой корм')])[2]")
corm.click()

"""Фильтрация и выбор товаров на странице corm_page"""
min_price = driver.find_element(By.XPATH, "//input[@id='arrFilter_P1_MIN']")
min_price.click()
min_price.send_keys("50")
min_price.send_keys(Keys.TAB)
time.sleep(3)

max_price = driver.find_element(By.XPATH, "//input[@id='arrFilter_P1_MAX']")
max_price.click()
max_price.send_keys("2000")
max_price.send_keys(Keys.TAB)
time.sleep(2)
driver.execute_script("window.scrollTo(0, 300);")


discount = driver.find_element(By.XPATH, "//label[contains(text(), 'ДА')]")
discount.click()

brand1 = driver.find_element(By.XPATH, "//label[contains(text(), '1st Choice ')]")
brand1.click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, 300);")

brand2 = driver.find_element(By.XPATH, "//label[contains(text(), 'Almo Nature ')]")
brand2.click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, 500);")

ingredients = driver.find_element(By.XPATH, "//label[contains(text(), 'Курица / Птица ')]")
ingredients.click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, 500);")

#Нужно сохранить название товара, что в принте вывести в меню какого товара осуществлен переход

corm_product = driver.find_element(By.XPATH, "(//div[@class='product-name'])[1]")
value_corm_product = corm_product.text
print(f"Выбран товар - {value_corm_product}")

corm_product.click()
print(f"Переход на страницу товара")
time.sleep(2)

#
"""Переход в персональную страницу товара №1"""
#сравнение назваий товара на персольной странице товара со страницы каталога товаров
header = driver.find_element(By.XPATH, "//h1[@class='card-title']")
value_header = header.text
print(f"Заголовок товара - {value_header}")

assert value_corm_product == value_header
print("Названия товара на персональной странице совпадает с названием товара в каталоге")


count_plus = driver.find_element(By.XPATH, "(//a[@class='count-btn plus'])[2]")
count_plus.click()
count_plus.click()
count_plus.click()

count_minus = driver.find_element(By.XPATH, "(//a[@class='count-btn minus'])[2]")
count_minus.click()

price_small = driver.find_element(By.XPATH, "(//div[@class='card__info__top card-price'])[2]")
value_price_small = price_small.text
print(f"Цена за маленькую упаковку корма - {value_price_small}")

# Извлечение числового значения из строки
price_number = re.sub(r'[^\d.]', '', value_price_small)  # оставляем только цифры и точку
etalon_price = float(price_number) * 2
print(etalon_price)


total_price = driver.find_element(By.XPATH, "//div[@id='element_total_price']")
value_total_price = total_price.text
# Извлечение числового значения из строки
total_number = re.sub(r'[^\d.]', '', value_total_price)  # оставляем только цифры и точку
print(f"Цена total_number - {total_number}")
value = float(total_number)
print(f'Итоговая цена - {value}')

assert etalon_price == value
print("Проверка итоговой цены за корм пройдена успешно")

basket = driver.find_element(By.XPATH, "//a[@id='basket_button']")
basket.click()
print("Сухой корм добавлен в корзину")


# fillers = driver.find_element(By.XPATH, "//div[contains(text(), 'Наполнители')]")
# fillers.click()
# time.sleep(2)
#
# brand_fillers_1 = driver.find_element(By.XPATH, "//label[contains(text(), 'Proline ')]")
# brand_fillers_1.click()
# time.sleep(2)
#
#
# brand_fillers_2 = driver.find_element(By.XPATH, "//label[contains(text(), 'CATRON ')]")
# brand_fillers_2.click()
# time.sleep(2)
#
# fillers_product = driver.find_element(By.XPATH, "(//div[@class='product-name'])[1]")
# fillers_product.click()
# print(f"Переход на страницу товара")
# time.sleep(2)
#
# """Переход в персональную страницу товара №2"""
# total_price_fillers = driver.find_element(By.XPATH, "//div[@id='element_total_price']")
# value_total_price_fillers = total_price_fillers.text
# # Извлечение числового значения из строки
# total_number_fillers = re.sub(r'[^\d.]', '', value_total_price_fillers)  # оставляем только цифры и точку
# print(f'Итоговая цена за наполнитель - {total_number_fillers}')
#
# basket = driver.find_element(By.XPATH, "//a[@id='basket_button']")
# basket.click()
# print("Наполнитель добавлен в корзину")
#




"""Переход в режим корзины"""
cart = driver.find_element(By.XPATH, "//a[@class='ownd-header-basket-block hidden-md']")
cart.click()
print("Переход в корзину")

"""Страница корзины"""
checkout = driver.find_element(By.XPATH, "(//a[@class='btn btn-yellow b-btn'])[2]")
checkout.click()



"""Страница оформления заказа"""
"""Заполняю все обязательные поля КРОМЕ ТЕЛЕФОНА, чтобы заказ не был оформлен. Ведь сайт не является тестовым"""
name = driver.find_element(By.XPATH, "//input[@name='ORDER_PROP_1']")
name.click()
name.send_keys("Пупкин Виталий Игоревич")

mail = driver.find_element(By.XPATH, "//input[@name='ORDER_PROP_2']")
mail.click()
mail.send_keys("fdhfghf@mail.ru")

# radio = driver.find_element(By.XPATH, "//label[@for='delivery_3']")
# radio.click()
driver.execute_script("window.scrollTo(0, 300);")

day = driver.find_element(By.XPATH, "(//div[@class='ownd-datetime-day disabled'])[1]")
day.click()

data_day = driver.find_element(By.XPATH, "(//*[@id='ownd-datetime']/div[1]/div[1]/span)[1]")
value_data_day = data_day.text
print(f"Пытаемся выбрать дату доставки на сегодня  - {value_data_day}")


delivery_date_fact = driver.find_element(By.XPATH, "//*[@id='ownd-datetime']/div[4]/div[1]/b")
value_delivery_date_fact = delivery_date_fact.text
print(f"Ближайшая доступная дата доставки - {value_delivery_date_fact}")

number_1 = re.findall(r'\d+', value_data_day)[0]
number_2 = re.findall(r'\d+', value_delivery_date_fact)[0]
print(number_1)
print(number_2)

try:
    assert number_1 == number_2
    print("Заказ будет доставлен сегодня")
except:
    print(f"  Курьер не сможет привезти заказ сегодня, самая ближайшая дата доставки, которую удалось выбрать - {value_delivery_date_fact}")


city = driver.find_element(By.XPATH, "//input[@name='ORDER_PROP_40']")
city.click()
city.send_keys("Санкт-Петербург")

street = driver.find_element(By.XPATH, "(//input[@name='ORDER_PROP_20'])[2]")
street.click()
street.send_keys("Ленина")

house = driver.find_element(By.XPATH, "(//input[@name='ORDER_PROP_21'])[2]")
house.click()
house.send_keys("2")

apartment = driver.find_element(By.XPATH, "//input[@name='ORDER_PROP_22']")
apartment.click()
apartment.send_keys("26")

driver.execute_script("window.scrollTo(0, 500);")

radio_payment = driver.find_element(By.XPATH, "//label[@for='radio_pay_4']")
radio_payment.click()

try:
    checkout_finish = driver.find_element(By.XPATH, "//a[@id='button_submit_order_ajax']")
    checkout_finish.click()
    print("Заказ оформлен")
except:
    print("Не заполнено одно из обязательных полей")

print("Тест выполнен")


















# """Отработка исключений"""
# filter = driver.find_element(By.XPATH, "(//div[@class='sc-fb980e9c-0 dZmSNe'])[2]")
# filter.click()
# print("успешно")
#
# time.sleep(2)
# min_price = driver.find_element(By.XPATH, "//input[@name='inputMin']")
# min_price.click()
# min_price.send_keys(Keys.CONTROL+"A")
# min_price.send_keys(Keys.DELETE)
# min_price.send_keys("999")
# min_price.send_keys(Keys.TAB)
#
# max_price = driver.find_element(By.XPATH, "//input[@name='inputMax']")
# max_price.send_keys(Keys.CONTROL+"A")
# max_price.send_keys(Keys.DELETE)
# max_price.send_keys("3000")
# max_price.send_keys(Keys.ENTER)
# time.sleep(1)
# color = driver.find_element(By.XPATH, "(//li[@class='sc-430132b1-1 dEQNzQ'])[1]")
# color.click()
# time.sleep(1)
# try:
#     white_color = driver.find_element(By.XPATH, "(//div[@class='sc-7100d96-0 GPyUb checkbox'])[2]")
#     white_color.click()
#     time.sleep(1)
# except:
#     print("Не выбран фильтр по цвету")
#
#
#
# try:
#     size = driver.find_element(By.XPATH, "(//li[@class='sc-430132b1-1 dEQNzQ'])[1]")
#     size.click()
#     time.sleep(1)
#     size_s = driver.find_element(By.XPATH, "//button[@data-testid='dimensions-button-2']")
#     size_s.click()
#
#     size_m = driver.find_element(By.XPATH, "//button[@data-testid='dimensions-button-3']")
#     size_m.click()
#     time.sleep(1)
# except:
#     print("Не выбран размер")
#
# spam_cookie = driver.find_element(By.XPATH, "//button[@class='sc-7d7c1299-1 sc-7d7c1299-2 eHeVh cPSfug']")
# spam_cookie.click()
#
# show = driver.find_element(By.XPATH, "//button[@class='sc-7d7c1299-1 sc-7d7c1299-8 fJovLH cDXDeW']")
# show.click()
# time.sleep(1)
#
# time.sleep(6)
# iframe_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//iframe[@id='fl-863600']")))
# driver.switch_to.frame(iframe_element)

# button_close = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Закрыть']")))
# button_close.click()











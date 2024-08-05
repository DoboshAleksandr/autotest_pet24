import time

import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.basket_page import BasketPage
from pages.cat_page import CatPage
from pages.fillers_page import FillersPage
from pages.main_page import MainPage
from pages.corm_page import CormPage
from pages.order_page import OrderPage
from pages.product_page import ProductPage



@allure.description("Test buy corm for cats")   #аннотация в отчете allure, того, чтобы мы будем делать
def test_buy_fillers_for_cats():
#     """Тест по покупке товара включает в себя: выбор товара, заполнение данных получателя, подтверждение покупки."""
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)       #чтобы браузер не закрывался после выполнения кода
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument("--headless")                              #чтобы браузер не запускался при выполнении кода
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    print("Start Test 2")

    mp = MainPage(driver)
    mp.select_animal()            # для перехода к товарам из раздела - Кошки

    ctp = CatPage(driver)
    ctp.select_fillers()           # метод для перехода к товарам из раздела - Наполнители

    fp = FillersPage(driver)
    fp.fillers_filter()            # метод для фильтрации товаров и перехода к странице товара

    pp = ProductPage(driver)
    pp.select_fillers_product()    # страница товара, определение заголовка товара и цены, переход в корзину

    bp = BasketPage(driver)
    bp.go_to_order_page()          # страница корзины, определение заголовка товара и цены, переход к оформлению

    op = OrderPage(driver)
    op.formalization_order()       # оформление товара, ввод персональных данных киента, выбо дата доставки, выбор способа оплаты

    print("Finish Test 2")
    # time.sleep(60)
    # driver.quit()                  # закроется страница браузера
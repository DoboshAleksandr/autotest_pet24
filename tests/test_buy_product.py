import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.basket_page import BasketPage
from pages.cat_page import CatPage
from pages.main_page import MainPage
from pages.corm_page import CormPage
from pages.order_page import OrderPage
from pages.product_page import ProductPage


# @pytest.mark.run(order=1)
def test_buy_corm_for_cats():
    """Тест по покупке товара включает в себя: выбор товара, заполнение данных получателя, подтверждение покупки."""
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True) #чтобы браузер не закрывался после выполнения кода
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    print("Start Test 1")

    mp = MainPage(driver)
    mp.select_animal()

    ctp = CatPage(driver)
    ctp.select_corm()

    crp = CormPage(driver)
    crp.corm_filter()

    pp = ProductPage(driver)
    pp.select_product()

    bp = BasketPage(driver)
    bp.go_to_order_page()

    op = OrderPage(driver)
    op.formalization_order()

#
#     fp = FinishPage(driver)
#     fp.finish()
#     print("Finish Test 1")
#     # time.sleep(5)

# @pytest.mark.run(order=1)

# def test_buy_fillers_for_cats():
#     """Тест по покупке товара включает в себя: выбор товара, заполнение данных получателя, подтверждение покупки."""
#     options = webdriver.ChromeOptions()
#     options.add_argument('--ignore-certificate-errors')
#     options.add_argument('--ignore-ssl-errors')
#     # options.add_experimental_option("detach", True) #чтобы браузер не закрывался после выполнения кода
#     options.add_experimental_option('excludeSwitches', ['enable-logging'])
#     g = Service()
#     driver = webdriver.Chrome(options=options, service=g)
#
#     print("Start Test 1")
#
#     mp = MainPage(driver)
#     mp.select_animal()
#
#     cp = CatPage(driver)
#     cp.select_fillers()  # метод для


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
driver.get('https://petfood24.ru/catalog/sukhoy-korm-dlya-koshek/')
driver.maximize_window()

actions = ActionChains(driver)




"""Переход в _page"""


# corm = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='col-lg-3 col-sm-6'])[1]")))
min_price = driver.find_element(By.XPATH, "//input[@id='arrFilter_P1_MIN']")
min_price.click()
min_price.send_keys("50")
min_price.send_keys(Keys.TAB)
print("Выставлена минимальная цена за корм")




# class CormPage(Base):         # потомок класса Base
#     """В данном классе выбирается категория товаров (например корм, консервы, шампуни)"""
#
#
#
# #Locators (локаторы элементов, которые находятся на странице Авторизации)
#     min_price = "//input[@id='arrFilter_P1_MIN']"
#     max_price = "//input[@id='arrFilter_P1_MAX']"



    # discount = "//label[contains(text(), 'ДА')]"
    # brand1 = "//label[contains(text(), '1st Choice ')]"
    # brand2 = "//label[contains(text(), 'Almo Nature ')]"
    # ingredients = "//label[contains(text(), 'Курица / Птица ')]"
    # corm_product = "(//div[@class='product-name'])[1]"




    #Getters
    # - методы, которые будут осуществлять поиск элементов, по локаторам, используя определенные условия поиска,
# и возвращающие результат данного поиска.
#     def get_min_price(self):
#         return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.min_price)))
#
#     def get_max_price(self):
#         return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.max_price)))
#
#
#
#
# # Actions
#     # - методы, которые будут принимать результат поиска от Getters и производить требуемой действие, например кликать
#     # или вводить требуемую информацию.(действия с элементами)
#     def select_min_price(self):
#         self.get_min_price().click().send_keys("50")
#         self.send_keys(Keys.TAB)
#         print("Выставлена минимальная цена за корм")
#
#     def select_max_price(self):
#         self.get_max_price().click().send_keys("2000").send_keys(Keys.TAB)
#         self.driver.execute_script("window.scrollTo(0, 300);")
#         print("Выставлена максимальная цена за корм")



















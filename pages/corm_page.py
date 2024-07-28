import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class CormPage(Base):         # потомок класса Base
    """На данной странице можно отфильтровать товары категории - Сухой корм"""


    #Locators
    min_price = "//input[@id='arrFilter_P1_MIN']"
    max_price = "//input[@id='arrFilter_P1_MAX']"
    discount = "//label[contains(text(), 'ДА')]"
    brand1 = "//label[contains(text(), '1st Choice ')]"
    brand2 = "//label[contains(text(), 'Almo Nature ')]"
    ingredients = "//label[contains(text(), 'Курица / Птица ')]"
    corm_product = "(//div[@class='product-name'])[1]"


    #Getters

    def get_min_price(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.min_price)))

    def get_max_price(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.max_price)))

    def get_discount(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.discount)))

    def get_brand1(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.brand1)))

    def get_brand2(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.brand2)))

    def get_ingredients(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.ingredients)))

    def get_corm_product(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.corm_product)))


    # Actions
    def select_min_price(self):
        self.get_min_price().click()
        self.get_min_price().clear()
        self.get_min_price().send_keys("50")       #min_price_elem
        self.get_min_price().send_keys(Keys.TAB)
        print("Выставлена минимальная цена за корм")
        time.sleep(2)

    def select_max_price(self):
        self.get_max_price().click()
        self.get_max_price().clear()
        self.get_max_price().send_keys("2000")
        self.get_max_price().send_keys(Keys.TAB)
        self.driver.execute_script("window.scrollTo(0, 300);")
        print("Выставлена максимальная цена за корм")
        time.sleep(2)

    def select_discount(self):
        self.get_discount().click()
        print("Выставлен фильтр - со скидкой")
        time.sleep(2)

    def select_brand1(self):
        self.get_brand1().click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 300);")
        print("Выбран производитель")
        time.sleep(2)

    def select_brand2(self):
        self.get_brand2().click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 500);")
        print("Выбран производитель")
        time.sleep(2)

    def select_ingredients(self):
        self.get_ingredients().click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 500);")
        print("Выбраны ингредиент")
        time.sleep(2)

    def select_corm_product(self):
        corm_product_element = self.get_corm_product()
        value_corm_product = corm_product_element.text
        print(f"Выбран товар - {value_corm_product}")
        corm_product_element.click()
        print("Переход на страницу товара")
        time.sleep(2)


    # Methods
    def corm_filter(self):
        self.get_current_url()
        self.select_min_price()                  #выбрана минимальная цена
        self.select_max_price()                  #выбрана максимальная цена
        self.select_discount()                   #выбрать чек-бокс "товары со скидкой"
        self.select_brand1()                     #товары бренда 1
        self.select_brand2()                     #товары бренда 2
        self.select_ingredients()                #товары с ингредиентом - Курица/птица
        self.select_corm_product()               #Переход на страницу товара











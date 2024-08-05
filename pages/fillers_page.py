import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class FillersPage(Base):         # потомок класса Base
    """На данной странице можно отфильтровать товары категории - Наполнители"""


    #Locators
    brand_fillers_1 = "//label[contains(text(), 'Proline ')]"
    brand_fillers_2 = "//label[contains(text(), 'CATRON ')]"
    fillers_product = "(//div[@class='product-name'])[1]"


    #Getters

    def get_brand_fillers_1(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.brand_fillers_1)))

    def get_brand_fillers_2(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.brand_fillers_2)))

    def get_fillers_product(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.fillers_product)))



    # Actions
    def select_brand_fillers_1(self):
        self.get_brand_fillers_1().click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 300);")
        print("Выбран производитель")
        time.sleep(2)

    def select_brand_fillers_2(self):
        self.get_brand_fillers_2().click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 500);")
        print("Выбран производитель")
        time.sleep(2)

    def select_fillers_product(self):
        self.get_fillers_product().click()
        print(f"Переход на страницу товара, наполнитель для кошек")
        time.sleep(2)


    # Methods
    def fillers_filter(self):
        with allure.step("Fillers filter"):  # аннотация в отчете allure, того, чтобы мы будем делать
            Logger.add_start_step(method="fillers_filter")
            self.get_current_url()
            self.select_brand_fillers_1()                  #показать товары бренда1
            self.select_brand_fillers_2()                  #показать товары бренда1
            self.select_fillers_product()                  #перейти на страницу выбранного товара
            Logger.add_end_step(url=self.driver.current_url, method="fillers_filter")











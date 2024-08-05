import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class CatPage(Base):
    """В данном классе выбирается категория товаров (например корм, консервы, шампуни)"""


    # Locators
    corm = "(//a[contains(text(), 'Сухой корм')])[2]"
    fillers = "//div[contains(text(), 'Наполнители')]"

    # Getters
    def get_corm(self):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.corm)))

    def get_fillers(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.fillers)))


    # Actions
    def click_corm(self):
        self.get_corm().click()
        time.sleep(2)
        print("Переход в раздел - Сухой корм")

    def click_fillers(self):
        self.get_fillers().click()
        time.sleep(2)
        print("Переход в раздел - Наполнители")


    # Methods
    def select_corm(self):
        with allure.step("Select corm"):        #аннотация в отчете allure, того, чтобы мы будем делать
            Logger.add_start_step(method="select_corm")
            self.get_current_url()
            self.click_corm()                  #переход к товарам раздела - Сухой корм
            Logger.add_end_step(url=self.driver.current_url, method="select_corm")


    def select_fillers(self):
        with allure.step("Select fillers"):        #аннотация в отчете allure, того, чтобы мы будем делать
            Logger.add_start_step(method="select_fillers")
            self.get_current_url()
            self.click_fillers()               #переход к товарам раздела - Наполнители
            Logger.add_end_step(url=self.driver.current_url, method="select_fillers")

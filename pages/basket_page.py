import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class BasketPage(Base):

    # Locators
    checkout = "(//a[@class='btn btn-yellow b-btn'])[2]"

    # Getters
    def get_checkout(self):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.checkout)))


    # Actions
    def click_checkout(self):
        self.get_checkout().click()
        time.sleep(2)
        print("Переход в режим оформления заказа")



    # Methods
    def go_to_order_page(self):
        with allure.step("Go to order page"):  # аннотация в отчете allure, того, чтобы мы будем делать
            Logger.add_start_step(method="go_to_order_page")
            self.get_current_url()
            self.click_checkout()                       # Переход в режим оформления заказа
            Logger.add_end_step(url=self.driver.current_url, method="go_to_order_page")



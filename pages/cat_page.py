import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base



class CatPage(Base):
    """В данном классе выбирается категория товаров (например корм, консервы, шампуни)"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators (локаторы элементов, которые находятся на странице)
    corm = "(//a[contains(text(), 'Сухой корм')])[2]"
    fillers = "//div[contains(text(), 'Наполнители')]"

    # Getters - методы, которые будут осуществлять поиск элементов, по локаторам, используя определенные условия поиска и возвращающие результат данного поиска.
    def get_corm(self):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.corm)))

    def get_fillers(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.fillers)))


    # Actions - методы, которые будут принимать результат поиска от Getters и производить требуемой действие, например кликать или вводить требуемую информацию.(действия с элементами)
    def click_corm(self):
        self.get_corm().click()
        time.sleep(2)
        print("Переход в раздел - Сухой корм")

    def click_fillers(self):
        self.get_fillers().click()
        time.sleep(2)
        print("Переход в раздел - Наполнители")


    # Methods - методы, содержащий список методов Actions, представленных в виде действий
    def select_corm(self):
        self.get_current_url()
        self.click_corm()                  #переход к товарам раздела - Сухой корм

    def select_fillers(self):
        self.get_current_url()
        self.click_fillers()               #переход к товарам раздела - Наполнители
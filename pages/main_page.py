import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class MainPage(Base):         # потомок класса Base
    """В данном классе выбирается вид домашнего питомца для которого подбираются товары (например кошка или собака)"""

    url = 'https://petfood24.ru/'
    def __init__(self, driver):
            super().__init__(driver)  # помощью super мы указываем, что это потомок
            self.driver = driver

#Locators (локаторы элементов, которые находятся на странице Авторизации)
    cats = "(//span[contains(text(), 'Кошки')])[1]"


#Getters - методы, которые будут осуществлять поиск элементов, по локаторам, используя определенные условия поиска и возвращающие результат данного поиска.
    def get_cats(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.cats)))


# Actions - методы, которые будут принимать результат поиска от Getters и производить требуемой действие с элементами, например клик или ввод информации.
    def click_cats(self):
        self.get_cats().click()
        print("Переход в раздел - КОШКИ")



#Methods - метод, содержащий список методов Actions, представленных в виде действий
    def select_animal(self):
        with allure.step("Select_animal"):        #аннотация в отчете allure, того, чтобы мы будем делать
            Logger.add_start_step(method="select_animal")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()                          #проверка текущй url
            self.click_cats()                               #переход в товары для кошек
            Logger.add_end_step(url=self.driver.current_url, method="select_animal")





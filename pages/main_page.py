import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class MainPage(Base):         # потомок класса Base
    """В данном классе выбирается вид домашнего питомца для которого подбираются товары (например кошка или собака)"""

    url = 'https://petfood24.ru/'
    def __init__(self, driver):
            super().__init__(driver)  # помощью super мы указываем, что это потомок
            self.driver = driver

#Locators (локаторы элементов, которые находятся на странице Авторизации)
    cats = "(//span[contains(text(), 'Кошки')])[1]"


#Getters
    # - методы, которые будут осуществлять поиск элементов, по локаторам, используя определенные условия поиска,
# и возвращающие результат данного поиска.
    def get_cats(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.cats)))


# Actions
    # - методы, которые будут принимать результат поиска от Getters и производить требуемой действие, например кликать
    # или вводить требуемую информацию.(действия с элементами)
    def click_cats(self):
        self.get_cats().click()
        print("Переход в раздел - КОШКИ")



#Methods
    #  - метод, содержащий список Actions, представленных в виде действий, например один метод
    #  может включать в себя несколько действий: вести логин, ввести пароль, нажать кнопку "Войти".
    def select_animal(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_cats()
        # self.assert_url(self, "https://petfood24.ru/catalog/tovary-dlya-koshek/")





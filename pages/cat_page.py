import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


# class CatPage(Base):         # потомок класса Base
#     """В данном классе выбирается категория товаров (например корм, консервы, шампуни)"""
#     # url = 'https://petfood24.ru/catalog/tovary-dlya-koshek/'
#     def __init__(self, driver):
#             super().__init__(driver)  # помощью super мы указываем, что это потомок
#             self.driver = driver
#
# #Locators (локаторы элементов, которые находятся на странице Авторизации)
#     corm = "(//a[contains(text(), 'Сухой корм')])[2]"
#     fillers = "//div[contains(text(), 'Наполнители')]"
#
#
# #Getters
#     # - методы, которые будут осуществлять поиск элементов, по локаторам, используя определенные условия поиска,
# # и возвращающие результат данного поиска.
#     def get_corm(self):
#         # return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.corm)))
#         return self.driver.find_element(By.XPATH, self.corm)
#
#     def get_fillers(self):
#         return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.fillers)))
#
# # Actions
#     # - методы, которые будут принимать результат поиска от Getters и производить требуемой действие, например кликать
#     # или вводить требуемую информацию.(действия с элементами)
#     def click_corm(self):
#         # self.driver.execute_script("window.scrollTo(0, 300);")
#         time.sleep(5)
#         self.get_corm().click()
#         print("Переход в раздел - Сухой корм")
#
#     # def click_fillers(self):
#     #     self.driver.execute_script("window.scrollTo(0, 300);")
#     #     time.sleep(2)
#     #     self.get_fillers().click()
#     #     print("Переход в раздел - Наполнители")
#
#
# #Methods
#     #  - метод, содержащий список Actions, представленных в виде действий, например один метод
#     #  может включать в себя несколько действий: вести логин, ввести пароль, нажать кнопку "Войти".
#     def select_corm(self):
#         # self.driver.get(self.url)
#         self.click_corm
#
#
#     # def select_fillers(self):
#     #     self.click_fillers



class CatPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

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

    # Methods
    def select_corm(self):
        self.get_current_url()
        self.click_corm()


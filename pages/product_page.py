import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class ProductPage(Base):         # потомок класса Base
    """Персональная страница товара, можно выбрать количество товара и добавить в корзину"""


#Locators
    header = "//h1[@class='card-title']"
    count_plus = "(//a[@class='count-btn plus'])[2]"
    count_minus = "(//a[@class='count-btn minus'])[2]"
    price_small = "(//div[@class='card__info__top card-price'])[2]"
    total_price = "//div[@id='element_total_price']"
    basket = "//a[@id='basket_button']"
    cart = "//a[@class='ownd-header-basket-block hidden-md']"


#Getters - методы, которые будут осуществлять поиск элементов, по локаторам, используя определенные условия поиска и возвращающие результат данного поиска.
    def get_header(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.header)))

    def get_count_plus(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.count_plus)))

    def get_count_minus(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.count_minus)))

    def get_price_small(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.price_small)))

    def get_total_price(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.total_price)))

    def get_basket(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.basket)))

    def get_cart(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.cart)))


# Actions
    def select_header(self):                                  #отображение назваия товара на персольной стр.
        header_element = self.get_header()
        value_header = header_element.text
        print(f"Заголовок на странице товара - {value_header}")


    def select_count_plus(self):                     #увеличиваем количество до трех
        self.get_count_plus().click()
        self.get_count_plus().click()
        self.get_count_plus().click()
        print("Увеличиваем количество товара до трех")

    def select_count_minus(self):                        #уменьшаем количество до двух
        self.get_count_minus().click()
        print("Уменьшаем количество товара до двух")

    def select_price_small(self):
        price_small_element = self.get_price_small()                                  # записывается значение цены за маленькую упаковку товара
        value_price_small = price_small_element.text
        print(f"Значение цены за маленькую упаковку товара - {value_price_small}")

        price_number = re.sub(r'[^\d.]', '', value_price_small)           # оставляем только цифры и точку
        self.etalon_price = float(price_number) * 2                                  # умножаем цену на 2 и узнаем цену за 2 товара - это Ожидаемая цена
        print(f"Значение ожидаемой цены за 2 товара - {self.etalon_price}")

    def select_total_price(self):
        # Узнаем итоговую цену и сравниваем её с Ожидаемой
        total_price_element = self.get_total_price()
        value_total_price = total_price_element.text                         # Извлечение числового значения из строки
        total_number = re.sub(r'[^\d.]', '', value_total_price)  # оставляем только цифры и точку
        print(f"Цена total_number - {total_number}")
        self.value = float(total_number)
        print(f'Итоговая цена за товар(ы) - {self.value}')

    def assert_price(self):
        assert self.etalon_price == self.value, f"Expected {self.etalon_price}, but got {self.value}"
        print("Значение итоговой цены за корм совпадает с ожидаемой, проверка пройдена успешно.")

    def select_basket(self):                         #Добавляем товар в корзину
        self.get_basket().click()
        print("Товар добавлен в корзину")

    def select_cart(self):                          #Переход в корзину
        self.get_cart().click()
        print("Переход в корзину")


# Methods
    def select_corm_product(self):
        self.get_current_url()                  # отображение текущей url
        self.select_header()                    # отображение заголовка товара
        self.select_count_plus()                # увеличиваем количество до трех
        self.select_count_minus()               # уменьшаем количество до двух
        self.select_price_small()               # значение цены за маленькую упаковку товара, умножаем цену на 2 и узнаем цену за 2 товара - это Ожидаемая цена
        self.select_total_price()               # итоговая / фактическая цена за корм
        self.assert_price()                     # сравнение ожидаемой цены с фактической
        self.select_basket()                    # товар добавлен в корзину
        self.select_cart()                      # переход в корзину


    def select_fillers_product(self):
        self.get_current_url()                  # отображение текущей url
        self.select_header()                    # отображение заголовка товара
        self.select_total_price()               # итоговая / фактическая цена за наполнитель
        self.select_basket()                    # товар добавлен в корзину
        self.select_cart()                      # переход в корзину
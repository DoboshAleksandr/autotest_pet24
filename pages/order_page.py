import re
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class OrderPage(Base):
    """Страница оформления заказа"""
    # Locators
    name = "//input[@name='ORDER_PROP_1']"
    mail = "//input[@name='ORDER_PROP_2']"
    day = "(//div[@class='ownd-datetime-day disabled'])[1]"
    data_day = "(//*[@id='ownd-datetime']/div[1]/div[1]/span)[1]"
    delivery_date_fact = "//*[@id='ownd-datetime']/div[4]/div[1]/b"
    city = "//input[@name='ORDER_PROP_40']"
    street = "(//input[@name='ORDER_PROP_20'])[2]"
    house = "(//input[@name='ORDER_PROP_21'])[2]"
    apartment = "//input[@name='ORDER_PROP_22']"
    radio_payment = "//label[@for='radio_pay_4']"
    checkout_finish = "//a[@id='button_submit_order_ajax']"

    # Getters
    def get_name(self):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.name)))

    def get_mail(self):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.mail)))

    def get_day(self):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.day)))

    def get_data_day(self):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.data_day)))

    def get_delivery_date_fact(self):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.delivery_date_fact)))

    def get_city(self):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.city)))

    def get_street(self):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.street)))

    def get_house(self):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.house)))

    def get_apartment(self):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.apartment)))

    def get_radio_payment(self):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.radio_payment)))

    def get_checkout_finish(self):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.checkout_finish)))



    # Actions
    def input_name(self):
        self.get_name().click()
        self.get_name().send_keys("Пупкин Виталий Игоревич")

    def input_mail(self):
        self.get_mail().click()
        self.get_mail().send_keys("fdhfghf@mail.ru")
        self.driver.execute_script("window.scrollTo(0, 300);")

    def click_day(self):
        self.get_day().click()

    def select_data_day(self):
        data_day_element = self.get_data_day()
        self.value_data_day = data_day_element.text
        print(f"Пытаемся выбрать дату доставки на сегодня  - {self.value_data_day}")

    def select_delivery_date_fact(self):
        date_fact_element = self.get_delivery_date_fact()
        self.value_date_fact = date_fact_element.text
        print(f"Ближайшая доступная дата доставки  - {self.value_date_fact}")

        number_1 = re.findall(r'\d+', self.value_data_day)[0]
        number_2 = re.findall(r'\d+', self.value_date_fact)[0]
        print(number_1)
        print(number_2)

        try:
            assert number_1 == number_2
            print("Заказ будет доставлен сегодня")
        except AssertionError:
            print(
                f"Курьер не сможет привезти заказ сегодня, самая ближайшая дата доставки, которую удалось выбрать - {self.value_date_fact}")

    def input_city(self):
        self.get_city().click()
        self.get_city().send_keys("Санкт-Петербург")

    def input_street(self):
        self.get_street().click()
        self.get_street().send_keys("Ленина")

    def input_house(self):
        self.get_house().click()
        self.get_house().send_keys("2")

    def input_apartment(self):
        self.get_apartment().click()
        self.get_apartment().send_keys("26")
        self.driver.execute_script("window.scrollTo(0, 500);")

    def click_radio_payment(self):
        self.get_radio_payment().click()

    def click_checkout_finish(self):
        try:
            self.get_checkout_finish().click()
            print("Заказ оформлен")
        except:
            print("Не заполнено одно из обязательных полей")

        print("Тест выполнен")




    # Methods
    """Заполнение всех обязательных полей КРОМЕ ТЕЛЕФОНА, чтобы заказ не был оформлен. Ведь сайт не является тестовым"""
    def formalization_order(self):
        self.get_current_url()
        self.input_name()
        self.input_mail()
        self.click_day()
        self.select_data_day()
        self.select_delivery_date_fact()
        self.input_city()
        self.input_street()
        self.input_house()
        self.input_apartment()
        self.click_radio_payment()
        self.click_checkout_finish()


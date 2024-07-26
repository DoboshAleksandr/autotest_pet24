import datetime

class Base():
    """Базовый класс, содержащий универсальные методы"""
    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""  #Метод который возвращает нам текущую url
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method assert word"""
    def assert_word(self, word, result):   #где word - заголовок страницы, для которого создана проверка, result - ожидаемый результат
        value_word = word.text
        assert value_word == result
        print("Good value word")


    """Method Screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\py_projects\\petfood24\\screen\\' + name_screenshot)

    """Method assert url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Значение URL совпадает с ожидаемым")
from selenium import webdriver
from page_object import HeaderPageYandexScooter, OrderPageYandexScooter1, \
    OrderPageYandexScooter2, HomePageYandexScooter
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ED
from selenium.webdriver.support.wait import WebDriverWait
import allure

class TestOrderScooter():
    driver = None
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Заказ самоката по кнопке "Заказать" в заголовке страницы')
    @allure.description('Заполняем обязательные поля в форме заказа и проверяем, '
                        'что в результате появляется сообщение об успешном оформлении заказа. ')
    def test_order_scooter_by_button_in_header(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        page_header = HeaderPageYandexScooter(self.driver)
        page_header.wait_for_load_header()
        page_header.click_button_order()
        page_order = OrderPageYandexScooter1(self.driver)
        page_order.wait_for_load_who_is_the_scooter_for()
        page_order.set_name('Лиса')
        page_order.set_surname('Алиса')
        page_order.set_address('Усачева, дом 3')
        page_order.set_metro('Фрунзенская')
        page_order.set_phone('88005005050')
        page_order.click_button_next()
        page_order2 = OrderPageYandexScooter2(self.driver)
        page_order2.wait_for_load_abort_rent()
        page_order2.set_date()
        page_order2.set_rental_period('сутки')
        page_order2.click_button_order()
        page_order2.wait_for_load_pop_up_window()
        page_order2.click_button_yes()
        page_order2.wait_for_load_order_creation()
        assert page_order2.order_creation


    @allure.title('Заказ самоката по кнопке "Заказать" в конце страницы.')
    @allure.description('Заполняем все поля в форме заказа и проверяем, '
                        'что в результате появляется сообщение об успешном оформлении заказа.')
    def test_order_scooter_by_button_on_page(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        page_home = HomePageYandexScooter(self.driver)
        page_home.wait_for_load_button_cookie()
        page_home.click_button_cookie()
        page_home.wait_for_load_button_order_on_page()
        page_home.click_button_order_on_page()
        page_order1 = OrderPageYandexScooter1(self.driver)
        page_order1.wait_for_load_who_is_the_scooter_for()
        page_order1.set_name('Фродо')
        page_order1.set_surname('Бегинс')
        page_order1.set_address('Комсомольский проспект, 18')
        page_order1.set_metro('Парк Культуры')
        page_order1.set_phone('89111234567')
        page_order1.click_button_next()
        page_order2 = OrderPageYandexScooter2(self.driver)
        page_order2.wait_for_load_abort_rent()
        page_order2.set_date()
        page_order2.set_rental_period('двое суток')
        page_order2.click_checkbox_black()
        page_order2.set_comment('Приезжай скорее')
        page_order2.click_button_order()
        page_order2.wait_for_load_pop_up_window()
        page_order2.click_button_yes()
        page_order2.wait_for_load_order_creation()
        assert page_order2.order_creation


    @allure.title('Проверка клика по логотипу "Самокат".')
    @allure.description('Проверяем, что при нажатии на логотип "Самокат" '
                        'на странице оформления заказа попадаешь на главную страницу.')
    def test_click_on_logo_scooter(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        page_header = HeaderPageYandexScooter(self.driver)
        page_header.wait_for_load_header()
        page_header.click_button_order()
        page_order = OrderPageYandexScooter1(self.driver)
        page_order.wait_for_load_who_is_the_scooter_for()
        page_header.click_logo_scooter()
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'


    @allure.title('Проверка клика по логотипу "Яндекс".')
    @allure.description('Проверяем, что при нажатии на логотип "Яндекс" '
                        'на странице оформления заказа в новом окне откроется главная страница Яндекса."')
    def test_click_on_logo_yandex(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        page_header = HeaderPageYandexScooter(self.driver)
        page_header.wait_for_load_header()
        page_header.click_button_order()
        page_order = OrderPageYandexScooter1(self.driver)
        page_order.wait_for_load_who_is_the_scooter_for()
        page_header.click_logo_yandex()
        page_header.switching_to_new_tab()
        WebDriverWait(self.driver, 3).until(ED.visibility_of_element_located((By.CLASS_NAME, 'dzen-desktop__search-37')))
        assert self.driver.current_url == 'https://dzen.ru/?yredirect=true'


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()




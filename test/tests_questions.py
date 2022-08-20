from selenium import webdriver
from page_object import HomePageYandexScooter
import allure

class TestQuestions():

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка ответа на вопрос "Сколько это стоит? И как оплатить?"')
    @allure.description('Ищем вопрос на странице и проверяем, '
                        'что текст ответа == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."')
    def test_question_1(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        page_home = HomePageYandexScooter(self.driver)
        page_home.wait_for_load_button_cookie()
        page_home.click_button_cookie()
        page_home.scroll_to_block_of_questions()
        page_home.click_on_question_1()
        text_response = page_home.get_text_response_1()
        assert text_response == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.title('Проверка ответа на вопрос "Хочу сразу несколько самокатов! Так можно?"')
    @allure.description('Ищем вопрос на странице и проверяем, что текст ответа == "Пока что у нас так: один заказ — один самокат. '
                        'Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим"')
    def test_question_2(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        page_home = HomePageYandexScooter(self.driver)
        page_home.scroll_to_block_of_questions()
        page_home.click_on_question_2()
        text_response = page_home.get_text_response_2()
        assert text_response == 'Пока что у нас так: один заказ — один самокат.' \
                                ' Если хотите покататься с друзьями, можете просто сделать' \
                                ' несколько заказов — один за другим.'

    @allure.title('Проверка ответа на вопрос "Как рассчитывается время аренды?"')
    @allure.description('Ищем вопрос на странице и проверяем, что текст ответа == "Допустим, вы оформляете заказ на 8 мая. '
                        'Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, '
                        'когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."')
    def test_question_3(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        page_home = HomePageYandexScooter(self.driver)
        page_home.scroll_to_block_of_questions()
        page_home.click_on_question_3()
        text_response = page_home.get_text_response_3()
        assert text_response == 'Допустим, вы оформляете заказ на 8 мая. ' \
                                'Мы привозим самокат 8 мая в течение дня. ' \
                                'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. ' \
                                'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    @allure.title('Проверка ответа на вопрос "Можно ли заказать самокат прямо на сегодня?"')
    @allure.description('Ищем вопрос на странице и проверяем, что текст ответа == "Только начиная с завтрашнего дня. '
                        'Но скоро станем расторопнее"')
    def test_question_4(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        page_home = HomePageYandexScooter(self.driver)
        page_home.scroll_to_block_of_questions()
        page_home.click_on_question_4()
        text_response = page_home.get_text_response_4()
        assert text_response == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.title('Проверка ответа на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"')
    @allure.description('Ищем вопрос на странице и проверяем, что текст ответа == "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку '
                        'по красивому номеру 1010."')
    def test_question_5(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        page_home = HomePageYandexScooter(self.driver)
        page_home.scroll_to_block_of_questions()
        page_home.click_on_question_5()
        text_response = page_home.get_text_response_5()
        assert text_response == 'Пока что нет! ' \
                                'Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    @allure.title('Проверка ответа на вопрос "Вы привозите зарядку вместе с самокатом?"')
    @allure.description('Ищем вопрос на странице и проверяем, что текст ответа == "Самокат приезжает к вам с полной зарядкой. '
                        'Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."')
    def test_question_6(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        page_home = HomePageYandexScooter(self.driver)
        page_home.scroll_to_block_of_questions()
        page_home.click_on_question_6()
        text_response = page_home.get_text_response_6()
        assert text_response == 'Самокат приезжает к вам с полной зарядкой. ' \
                                'Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. ' \
                                'Зарядка не понадобится.'

    @allure.title('Проверка ответа на вопрос ""Можно ли отменить заказ?')
    @allure.description('Ищем вопрос на странице и проверяем, что текст ответа == "Да, пока самокат не привезли. Штрафа не будет, '
                        'объяснительной записки тоже не попросим. Все же свои."')
    def test_question_7(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        page_home = HomePageYandexScooter(self.driver)
        page_home.scroll_to_block_of_questions()
        page_home.click_on_question_7()
        text_response = page_home.get_text_response_7()
        assert text_response == 'Да, пока самокат не привезли. ' \
                                'Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    @allure.title('Проверка ответа на вопрос "Я живу за МКАДом, привезёте?"')
    @allure.description('Ищем вопрос на странице и проверяем, что текс ответа == "Да, обязательно. Всем самокатов! '
                        'И Москве, и Московской области."')
    def test_question_8(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        page_home = HomePageYandexScooter(self.driver)
        page_home.scroll_to_block_of_questions()
        page_home.click_on_question_8()
        text_response = page_home.get_text_response_8()
        assert text_response == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
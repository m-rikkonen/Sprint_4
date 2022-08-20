from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ED
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys



class HeaderPageYandexScooter():
    button_order_in_header = [By.XPATH, ".//button[@class='Button_Button__ra12g']"]
    logo_yandex = [By.XPATH, ".//img[@alt='Yandex']"]
    logo_scooter = [By.XPATH, ".//img[@alt='Scooter']"]

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_header(self):
        WebDriverWait(self.driver, 3).until(ED.visibility_of_element_located(self.button_order_in_header))

    def click_button_order(self):
        self.driver.find_element(*self.button_order_in_header).click()

    def click_logo_yandex(self):
        self.driver.find_element(*self.logo_yandex).click()

    def click_logo_scooter(self):
        self.driver.find_element(*self.logo_scooter).click()

    def switching_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])


class OrderPageYandexScooter1:
    page_who_is_the_scooter_for = [By.XPATH, ".//div[text()='Для кого самокат']"]
    name_field = [By.XPATH, ".//div[1]/input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN']"]
    surname_field =[By.XPATH, ".//div[2]/input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN']"]
    address_field = [By.XPATH, ".//div[3]/input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN']"]
    metro_field = [By.XPATH, ".//input[@class='select-search__input']"]
    metro_option = [By.XPATH, ".//div[@class='select-search__select']/ul/li[1]"]
    phone_field = [By.XPATH, ".//div[5]/input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN']"]
    button_next = [By.XPATH, ".//button[text()='Далее']"]

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_who_is_the_scooter_for(self):
        WebDriverWait(self.driver, 3).until(ED.visibility_of_element_located(self.page_who_is_the_scooter_for))

    def set_name(self, name):
        self.driver.find_element(*self.name_field).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*self.surname_field).send_keys(surname)

    def set_address(self, address):
        self.driver.find_element(*self.address_field).send_keys(address)

    def set_metro(self, metro):
        self.driver.find_element(*self.metro_field).click()
        self.driver.find_element(*self.metro_field).send_keys(metro)
        WebDriverWait(self.driver, 3).until(ED.visibility_of_element_located(self.metro_option))
        self.driver.find_element(*self.metro_option).click()

    def set_phone(self, phone):
        self.driver.find_element(*self.phone_field).send_keys(phone)

    def click_button_next(self):
        self.driver.find_element(*self.button_next).click()

class OrderPageYandexScooter2:
    page_about_rent = [By.XPATH, ".//div[text()='Про аренду']"]
    date_field = [By.XPATH, ".//div[@class='Order_MixedDatePicker__3qiay']//input"]
    rental_field = [By.CLASS_NAME, 'Dropdown-root']
    rental_option = [By.XPATH, ".//div[@class='Dropdown-menu']/div[2]"]
    checkbox_black = [By.ID, 'black']
    checkbox_grey = [By.ID, 'grey']
    comment_field = [By.XPATH, ".//div[4]/input"]
    button_order = [By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']"]
    pop_up_window = [By.XPATH, ".//div[text()='Хотите оформить заказ?']"]
    button_yes = [By.XPATH, ".//button[text()='Да']"]
    order_creation = [By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ']"]

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_abort_rent(self):
        WebDriverWait(self.driver, 3).until(ED.visibility_of_element_located(self.page_about_rent))

    def set_date(self, date):
        self.driver.find_element(*self.date_field).send_keys(date)
        self.driver.find_element(*self.date_field).send_keys(Keys.ENTER)

    def set_rental_period(self, rental_period):
        self.driver.find_element(*self.rental_field).click()
        self.driver.find_element(*self.rental_option).click()

    def click_checkbox_black(self):
        self.driver.find_element(*self.checkbox_black).click()

    def click_checkbox_grey(self):
        self.driver.find_element(*self.checkbox_grey).click()

    def set_comment(self, comment):
        self.driver.find_element(*self.comment_field).send_keys(comment)

    def click_button_order(self):
        self.driver.find_element(*self.button_order).click()

    def wait_for_load_pop_up_window(self):
        WebDriverWait(self.driver, 3).until(ED.visibility_of_element_located(self.pop_up_window))

    def click_button_yes(self):
        self.driver.find_element(*self.button_yes).click()

    def wait_for_load_order_creation(self):
        WebDriverWait(self.driver, 3).until(ED.visibility_of_element_located(self.order_creation))


class HomePageYandexScooter:
    button_cookie = [By.ID, 'rcc-confirm-button']
    button_order_on_page = [By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button"]
    block_of_questions = [By.CLASS_NAME, 'Home_FAQ__3uVm4']
    button_question_1 = [By.ID, 'accordion__heading-0']
    text_response_1 = [By.ID, 'accordion__panel-0']
    button_question_2 = [By.ID, 'accordion__heading-1']
    text_response_2 = [By.ID, 'accordion__panel-1']
    button_question_3 = [By.ID, 'accordion__heading-2']
    text_response_3 = [By.ID, 'accordion__panel-2']
    button_question_4 = [By.ID, 'accordion__heading-3']
    text_response_4 = [By.ID, 'accordion__panel-3']
    button_question_5 = [By.ID, 'accordion__heading-4']
    text_response_5 = [By.ID, 'accordion__panel-4']
    button_question_6 = [By.ID, 'accordion__heading-5']
    text_response_6 = [By.ID, 'accordion__panel-5']
    button_question_7 = [By.ID, 'accordion__heading-6']
    text_response_7 = [By.ID, 'accordion__panel-6']
    button_question_8 = [By.ID, 'accordion__heading-7']
    text_response_8 = [By.ID, 'accordion__panel-7']


    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_button_cookie(self):
        WebDriverWait(self.driver, 3).until(ED.visibility_of_element_located(self.button_cookie))

    def click_button_cookie(self):
        self.driver.find_element(*self.button_cookie).click()

    def wait_for_load_button_order_on_page(self):
        WebDriverWait(self.driver, 3).until(ED.visibility_of_element_located(self.button_order_on_page))

    def click_button_order_on_page(self):
        self.driver.find_element(*self.button_order_on_page).click()

    def scroll_to_block_of_questions(self):
        element = self.driver.find_element(*self.block_of_questions)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_on_question_1(self):
        self.driver.find_element(*self.button_question_1).click()

    def get_text_response_1(self):
        return self.driver.find_element(*self.text_response_1).text

    def click_on_question_2(self):
        self.driver.find_element(*self.button_question_2).click()

    def get_text_response_2(self):
        return self.driver.find_element(*self.text_response_2).text

    def click_on_question_3(self):
        self.driver.find_element(*self.button_question_3).click()

    def get_text_response_3(self):
        return self.driver.find_element(*self.text_response_3).text

    def click_on_question_4(self):
        self.driver.find_element(*self.button_question_4).click()

    def get_text_response_4(self):
        return self.driver.find_element(*self.text_response_4).text

    def click_on_question_5(self):
        self.driver.find_element(*self.button_question_5).click()

    def get_text_response_5(self):
        return self.driver.find_element(*self.text_response_5).text

    def click_on_question_6(self):
        self.driver.find_element(*self.button_question_6).click()

    def get_text_response_6(self):
        return self.driver.find_element(*self.text_response_6).text

    def click_on_question_7(self):
        self.driver.find_element(*self.button_question_7).click()

    def get_text_response_7(self):
        return self.driver.find_element(*self.text_response_7).text

    def click_on_question_8(self):
        self.driver.find_element(*self.button_question_8).click()

    def get_text_response_8(self):
        return self.driver.find_element(*self.text_response_8).text









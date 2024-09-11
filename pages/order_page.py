from selenium.webdriver.common.by import By

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage(BasePage):
    def click_order_button(self):
        self.click_element(OrderPageLocators.order_button_top)

    def wait_for_order_form(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderPageLocators.name_field))

    def fill_order_form(self, name, surname, address, metro_station, phone, date, rental_period, color, comment):
        self.fill_field(OrderPageLocators.name_field, name)

        self.fill_field(OrderPageLocators.surname_field, surname)

        self.fill_field(OrderPageLocators.address_field, address)

        metro_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.metro_field)
        )
        metro_input.click()
        metro_input.send_keys(metro_station)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), '{metro_station}')]"))).click()

        self.fill_field(OrderPageLocators.phone_field, phone)

        self.click_element(OrderPageLocators.next_button)

        self.click_element(OrderPageLocators.date_field)

        calendar_date_xpath = f"//div[contains(@aria-label, 'пятница, 6-е сентября 2024 г.')]"
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, calendar_date_xpath))).click()

        self.click_element(OrderPageLocators.rental_period)
        rental_option_xpath = f"//div[contains(@class, 'Dropdown-option') and text()='{rental_period}']"
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, rental_option_xpath))).click()

        if color == 'black':
            self.click_element(OrderPageLocators.color_black)
        elif color == 'grey':
            self.click_element(OrderPageLocators.color_grey)

        self.fill_field(OrderPageLocators.comment_field, comment)

    def submit_order(self):
        self.click_element(OrderPageLocators.order_button)
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(OrderPageLocators.confirm_button)).click()

    def check_order_confirmation(self):
        confirmation_message = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(OrderPageLocators.order_confirmation_message))
        return "Заказ оформлен" in confirmation_message.text
from selenium.webdriver.common.by import By

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage(BasePage):
    def click_order_button(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON_TOP)

    def wait_for_order_form(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderPageLocators.NAME_FIELD))

    def fill_order_form(self, name, surname, address, metro_station, phone, date, rental_period, color, comment):
        self.fill_field(OrderPageLocators.NAME_FIELD, name)

        self.fill_field(OrderPageLocators.SURNAME_FIELD, surname)

        self.fill_field(OrderPageLocators.ADDRESS_FIELD, address)

        metro_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.METRO_FIELD)
        )
        metro_input.click()
        metro_input.send_keys(metro_station)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), '{metro_station}')]"))).click()

        self.fill_field(OrderPageLocators.PHONE_FIELD, phone)

        self.click_element(OrderPageLocators.NEXT_BUTTON)

        self.click_element(OrderPageLocators.DATE_FIELD)

        calendar_date_xpath = f"//div[contains(@class, 'keyboard-selected')]"
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, calendar_date_xpath))).click()

        self.click_element(OrderPageLocators.RENTAL_PERIOD)
        rental_option_xpath = f"//div[contains(@class, 'Dropdown-option') and text()='{rental_period}']"
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, rental_option_xpath))).click()

        if color == 'black':
            self.click_element(OrderPageLocators.COLOR_BLACK)
        elif color == 'grey':
            self.click_element(OrderPageLocators.COLOR_GREY)

        self.fill_field(OrderPageLocators.COMMENT_FIELD, comment)

    def submit_order(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(OrderPageLocators.CONFIRM_BUTTON)).click()

    def check_order_confirmation(self):
        confirmation_message = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(OrderPageLocators.ORDER_CONFIRMATION_MESSAGE))
        return "Заказ оформлен" in confirmation_message.text
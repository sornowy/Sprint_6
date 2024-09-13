from selenium.webdriver.common.by import By

from locators.question_page_locators import QuestionLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = QuestionLocators

    def wait_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        element = self.wait_element(locator)
        element.click()

    def fill_field(self, locator, value, timeout=10):
        field = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        field.clear()
        field.send_keys(value)

    def scroll_to_element(self, locator):
        element = self.wait_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)


class QuestionSection(BasePage):
    def scroll_to_section(self, index):
        question_locator = self.locators.QUESTIONS[index]
        self.scroll_to_element(question_locator)

    def click_question(self, index):
        question_locator = QuestionLocators.QUESTIONS[index]
        self.click_element(question_locator)

    def get_answer_text(self, index):
        answer_locator = QuestionLocators.ANSWER_PANEL[index]
        return self.wait_element(answer_locator).text


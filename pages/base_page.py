from selenium.webdriver.common.by import By

from locators.question_page_locators import QuestionLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()

    def fill_field(self, locator, value, timeout=10):
        field = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        field.clear()
        field.send_keys(value)

class QuestionSection(BasePage):
    def scroll_to_section(self):
        section_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(QuestionLocators.section))
        self.driver.execute_script("arguments[0].scrollIntoView();", section_element)

    def click_question(self, index):
        self.click_element((By.ID, f"accordion__heading-{index}"))

    def get_answer_text(self, index):
        answer_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, f"accordion__panel-{index}")))
        return answer_element.text

    def click_cookie_button(self):
        self.click_element((By.CLASS_NAME, "App_CookieButton__3cvqF"))

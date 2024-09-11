from selenium.webdriver.common.by import By

class QuestionLocators:
    section = (By.CSS_SELECTOR, "[class*='Home_FourPart']")
    question = (By.XPATH, '//div[contains(@id, "accordion__heading-")]')
    answer_panel = (By.XPATH, '//div[contains(@id, "accordion__panel-")]')
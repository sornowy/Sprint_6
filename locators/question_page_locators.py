from selenium.webdriver.common.by import By


class QuestionLocators:
    SECTION = (By.CSS_SELECTOR, "[class*='Home_FourPart']")
    QUESTIONS = [(By.ID, f'accordion__heading-{i}') for i in range(8)]
    ANSWER_PANEL = [(By.XPATH, f'.//*[@id="accordion__panel-{i}"]/p') for i in range(8)]



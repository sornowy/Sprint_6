from selenium.webdriver.common.by import By

class OrderPageLocators:
    ORDER_BUTTON_TOP = (By.CSS_SELECTOR, "[class*='Header_Nav'] [class*='Button_Button']")
    ORDER_BUTTON_BOTTOM = (By.CSS_SELECTOR, "[class*='Home_FinishButton'] [class*='Button_Button']")
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.CLASS_NAME, "select-search__input")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(), 'Далее')]")
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.CLASS_NAME,"Dropdown-placeholder")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(), 'Да')]")
    ORDER_CONFIRMATION_MESSAGE = (By.CSS_SELECTOR, "[class*='Order_ModalHeader']")
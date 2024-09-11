from selenium.webdriver.common.by import By

class OrderPageLocators:
    order_button_top = (By.CSS_SELECTOR, "[class*='Header_Nav'] [class*='Button_Button']")
    order_button_bottom = (By.CSS_SELECTOR, "[class*='Home_FinishButton'] [class*='Button_Button']")
    name_field = (By.XPATH, "//input[@placeholder='* Имя']")
    surname_field = (By.XPATH, "//input[@placeholder='* Фамилия']")
    address_field = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    metro_field = (By.CLASS_NAME, "select-search__input")
    phone_field = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    next_button = (By.XPATH, "//button[contains(text(), 'Далее')]")
    date_field = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    rental_period = (By.CLASS_NAME,"Dropdown-placeholder")
    color_black = (By.ID, "black")
    color_grey = (By.ID, "grey")
    comment_field = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    order_button = (By.XPATH, "//div[contains(@class, 'Order_Buttons__1xGrp')]//button[text()='Заказать']")
    confirm_button = (By.XPATH, "//button[contains(text(), 'Да')]")
    order_confirmation_message = (By.CSS_SELECTOR, "[class*='Order_ModalHeader']")
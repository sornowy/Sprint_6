from selenium.webdriver.common.by import By

class LogoPageLocators:
    SCOOTER_LOGO = (By.CSS_SELECTOR, "[class*='Header_LogoScooter']")
    YANDEX_LOGO = (By.CSS_SELECTOR, "[class*='Header_LogoYandex']")
    HOME_URL = 'https://qa-scooter.praktikum-services.ru/'
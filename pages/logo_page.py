
from locators.logo_page_locators import LogoPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogoPage(BasePage):
    def click_scooter_logo(self):
        self.click_element(LogoPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(LogoPageLocators.YANDEX_LOGO)

        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

        WebDriverWait(self.driver, 10).until(EC.url_contains("dzen.ru"))

    def get_home_url(self):
        return LogoPageLocators.HOME_URL
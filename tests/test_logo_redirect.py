import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from pages.logo_page import LogoPage

@pytest.mark.usefixtures("driver")
class TestLogoRedirects:

    @allure.feature("Проверка логотипа 'Самоката'")
    @allure.description("Тест проверяет, что клик по логотипу 'Самоката' перенаправляет на главную страницу")
    def test_scooter_logo_redirect(self, driver):
        logo_page = LogoPage(driver)
        logo_page.click_scooter_logo()
        assert driver.current_url == logo_page.get_home_url(), "Не удалось перейти на главную страницу!"

    @allure.feature("Проверка логотипа 'Яндекса'")
    @allure.description("Тест проверяет, что клик по логотипу 'Яндекса' открывает страницу Дзена в новой вкладке")
    def test_yandex_logo_redirect(self, driver):
        logo_page = LogoPage(driver)
        with allure.step("Кликнуть по логотипу 'Яндекса'"):
            logo_page.click_yandex_logo()

        with allure.step("Ждать появления новой вкладки"):
            WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)

        with allure.step("Переключиться на новую вкладку"):
            driver.switch_to.window(driver.window_handles[-1])

        with allure.step("Проверить, что открылась страница 'Дзена'"):
            assert "dzen.ru" in driver.current_url, "Не удалось открыть страницу Дзена!"
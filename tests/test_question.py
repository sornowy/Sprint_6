import  pytest
import allure
from pages.base_page import QuestionSection

@pytest.mark.usefixtures("driver")

class TestQuestionSection:

    @allure.feature("Проверка раздела 'Вопросы о важном'")
    @allure.story("Проверка корректности вопросов и ответов")
    def test_question_answer(self, driver):
        question = QuestionSection(driver)
        question.scroll_to_section()
        question.click_cookie_button()

        questions_answers = [
            (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
            (1, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
            (2, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
            (3, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
            (4, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
            (5, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
            (6, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
            (7, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")]

        for index, expected_answer in questions_answers:
            question.click_question(index)
            answer_text = question.get_answer_text(index)
            assert expected_answer in answer_text, f"Ответ для вопроса {index} не совпадает!"
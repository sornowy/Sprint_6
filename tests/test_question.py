import pytest
import allure
from pages.base_page import QuestionSection
from variables import questions_answers


@pytest.mark.usefixtures("driver")
class TestQuestionSection:

    @allure.feature("Проверка раздела 'Вопросы о важном'")
    @allure.story("Проверка корректности вопросов и ответов")
    @pytest.mark.parametrize("question_index, expected_answer", questions_answers)
    def test_question_answer(self, driver, question_index, expected_answer):
        question = QuestionSection(driver)

        with allure.step("Клик на Вопросы о важном"):
            question.scroll_to_section(question_index)
            question.click_question(question_index)

        with allure.step("Получение ответа из Вопросы о важном"):
            answer_text = question.get_answer_text(question_index)

        with allure.step("Сравнение полученного ответа с ожидаемым ответом на Вопрос"):
            assert answer_text == expected_answer, f"Expected '{expected_answer}', but got '{answer_text}'"
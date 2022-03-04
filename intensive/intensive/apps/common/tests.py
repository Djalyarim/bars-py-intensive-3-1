import json

from common.management.commands.products import (
    create_products,
)
from common.management.commands.recipes import (
    create_recipes,
)
from common.management.commands.users import (
    create_users,
)
from django.test import (
    TestCase,
)
from utils.helpers import (
    ordered,
)


class CommonTest(TestCase):
    """
    Тесты заданий
    """

    @classmethod
    def setUpTestData(cls):
        """
        Наполнение тестовой базы данных данными
        """
        create_users()
        create_products()
        create_recipes()

    def test_task_1(self):
        """
        Тест первого задания
        """
        response = self.client.get('/task-1/')

        trust_result = json.loads(
            '{"recipes": [["user4@pee.rocks", "Рецепт 1", "Описание рецепта 1"], ["user4@pee.rocks", "Рецепт 2", '
            '"Описание рецепта 2"], ["user4@pee.rocks", "Рецепт 3", "Описание рецепта 3"], ["user5@pee.rocks", '
            '"Рецепт 4", "Описание рецепта 4"], ["user5@pee.rocks", "Рецепт 5", "Описание рецепта 5"]]}'
        )

        response_result = json.loads(response.content)

        self.assertEqual(ordered(trust_result), ordered(response_result))

    def test_task_2(self):
        """
        Тест второго задания
        """
        response = self.client.get('/task-2/')

        trust_result = json.loads(
            '{"recipe_data": {"steps": [["Рецепт 1 Шаг 1", "Описание Рецепта 1 Шаг 1"], ["Рецепт 1 Шаг 3", '
            '"Описание Рецепта 1 Шаг 3"], ["Рецепт 1 Шаг 2", "Описание Рецепта 1 Шаг 2"]], '
            '"products": [["Минеральная вода", "Минеральная вода", "1.00", "л"], ["Масло растительное", '
            '"Масло растительное рафинированное", "1.00", "л"], ["Молоко", "Молоко 3.2%", "2.00", "л"], '
            '["Мясо говяжье", "Мясо говяжье", "3.00", "г"], ["Сахар", "Сахар", "1.00", "г"]]}}'
        )

        response_result = json.loads(response.content)

        self.assertEqual(ordered(trust_result), ordered(response_result))

    def test_task_3(self):
        """
        Тест третьего задания
        """
        response = self.client.get('/task-3/')

        trust_result = json.loads(
            '{"recipes": [["user4@pee.rocks", "Рецепт 3", "Описание рецепта 3", 2], ["user4@pee.rocks", "Рецепт 1", '
            '"Описание рецепта 1", 2], ["user4@pee.rocks", "Рецепт 2", "Описание рецепта 2", 1], ["user5@pee.rocks", '
            '"Рецепт 5", "Описание рецепта 5", 1], ["user5@pee.rocks", "Рецепт 4", "Описание рецепта 4", 1]]}'
        )

        response_result = json.loads(response.content)

        self.assertEqual(ordered(trust_result), ordered(response_result))

    def test_task_4(self):
        """
        Тест четвертого задания
        """
        response = self.client.get('/task-4/')

        trust_result = json.loads(
            '{"data": {"authors": [["Автор", "user4@pee.rocks", 3], ["Автор", "user5@pee.rocks", 2]], '
            '"voters": [["Пользователь", "user2@pee.rocks", 4], ["Пользователь", "user1@pee.rocks", 3], '
            '["Пользователь", "admin@pee.rocks", 0]]}}'
        )

        response_result = json.loads(response.content)

        self.assertEqual(ordered(trust_result), ordered(response_result))

    def test_task_5(self):
        """
        Тест пятого задания
        """
        response = self.client.get('/task-5/')

        trust_result = json.loads(
            '{"recipe_products": [["Рецепт 3", "Описание рецепта 3", "Масло растительное", "15.00", "л"], ["Рецепт 3", '
            '"Описание рецепта 3", "Молоко", "25.00", "л"], ["Рецепт 3", "Описание рецепта 3", "Картофель", "5000.00", '
            '"г"], ["Рецепт 3", "Описание рецепта 3", "Мясо говяжье", "5000.00", "г"], ["Рецепт 3", '
            '"Описание рецепта 3", "Сахар", "60.00", "г"], ["Рецепт 3", "Описание рецепта 3", "Соль", "110.00", "г"]]}'
        )

        response_result = json.loads(response.content)

        self.assertEqual(ordered(trust_result), ordered(response_result))





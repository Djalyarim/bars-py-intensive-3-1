import json
import sys
import time

from django.db import connection
from django.http import HttpResponse, JsonResponse
from django.utils.deprecation import MiddlewareMixin


class StatisticMiddleware:
    """
    Компонент вычисляющий время выполнения запроса на сервере и размер ответа в байтах.
    Отображает значения в консоли приложения
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.perf_counter()
        response = self.get_response(request)
        print(f'Время вычисления запроса {request} - {time.perf_counter() - start_time} секунд')
        print(f'Размер ответа - {sys.getsizeof(response.content)} байт')

        return HttpResponse(response)


class FormatterMiddleware:
    """
    Компонент форматирующий Json ответ в HttpResponse
    {'key': value} => <p>key = value</p>
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if isinstance(response, JsonResponse):
            data = ''
            parsed = json.loads(response.content)

            for key, value in parsed.items():
                data += f'<p>{key} = {value}</p>'
            response.content = data

        return HttpResponse(response)


class CheckErrorMiddleware(MiddlewareMixin):
    """
        Перехватывает необработанное исключение в представлении и отображает ошибку в виде
        "Ошибка: {exception}"
    """

    def process_exception(self, request, exception):

        error_message = f'Ошибка: {exception.args[0]}'
        response = HttpResponse(status=400, content=error_message)

        return response


class CheckQueriesMiddleware:
    """
    Выводит в консоль веб приложения все sql запросы к БД выполненные во время http-запроса.
    Отображает значения в консоли приложения.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        for query in connection.queries:
            print(query)

        return HttpResponse(response)

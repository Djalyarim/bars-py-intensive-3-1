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
        print(f'Размер ответа - {sys.getsizeof(response.content)} байт', '\n')

        return HttpResponse(response)


class CheckQueriesMiddleware:
    """
    Выводит в консоль веб приложения все sql запросы к БД выполненные во время http-запроса.
    Отображает значения в консоли приложения.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        __import__('pdb').set_trace()
        for query in connection.queries:
            print(query)

        return HttpResponse(response)

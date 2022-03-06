import json
from datetime import date

from django.db.models import Count, Min, Sum
from django.http import HttpResponse, JsonResponse

from day_10.models import Customer, OrderItem


def calc(request):
    """
    Представление которому в параметре запроса maths через разделитель
    перечисляются простейшие арифметические операции например
    maths=3*3,10-2,10/5 по умолчанию в качестве символа разделителя выступает
    сивол запятой. В необязательном параметре delimiter указывается символ
    разделителя арифметических операций
    например calc/?maths=3*3;10-2;10/5&delimiter=;

    Результат:  JsonResponse вида {'3*3': 9, '10-2': 8, '10/5': 2}
    """
    if not request.method == 'GET':
        print('Необходим запрос "GET"')
    if 'maths' not in request.GET:
        print('Отсутствует параметр "maths"')

    data = {}
    splitter = request.GET.get('delimiter', ',')
    set_of_expressions = request.GET['maths'].split(splitter)

    for value in set_of_expressions:
        data[value] = eval(value)

    response = JsonResponse(data, safe=False)

    return response


def query(request):
    """ Делаем несколько запросов к БД """

    query = list(
        Customer.objects.filter(
            order__date_formation__range=[date(2021, 1, 1), date(2021, 3, 31)]
        ).annotate(
            cnt=Count('order'),
            order_before=Min('order__date_formation')
        ).values_list(
            'name', 'cnt'
        ).order_by(
            '-cnt', 'order_before', 'name'
        ).first()
    )

    item = list(
        OrderItem.objects.filter(
            order__date_formation__range=[date(2021, 2, 1), date(2021, 3, 15)]
        ).values_list(
            'product__name'
        ).annotate(
            amount=Sum('count')
        ).order_by(
            '-amount'
        ).first()
    )

    response = HttpResponse(
        content=json.dumps(dict(query=query, item=item),
                           ensure_ascii=False,
                           default=str
                           )
    )

    return response

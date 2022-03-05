from django.http import HttpResponse, JsonResponse

from day_10.models import ProductCost, ProductCount


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
    sausage_cost = ProductCost.objects.all().values_list()
    ProductCount.objects.all().values().count()

    return HttpResponse(sausage_cost)

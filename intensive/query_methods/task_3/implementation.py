from unittest import result
from query_methods.models import Order, OrderItem, ProductCost, ProductCount
from django.db.models import Count, Sum, F


def get_top_order_by_sum_in_period(begin, end):
    """Возвращает заказ, который имеют наибольшую сумму за определенный промежуток времени
            Напишите функцию, которая выводит заказ с наибольшей общей суммой за период.
            Если несколько заказов имеют одинаковую сумму - вывести тот, чей номер больше.
    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает номер заказа и его сумму
    """

    order_with_max_cost = OrderItem.objects.filter(
        order__date_formation__range=(
            begin,
            end
        )
    ).filter(
        order__date_formation__range=(
            F('product__productcost__begin'),
            F('product__productcost__end')
        )
    ).values_list(
        'order__number'
    ).annotate(
        cost=Sum(F('count') * F('product__productcost__value'))
    ).order_by(
        '-cost',
        'order__number'
    ).first()

    return order_with_max_cost

from query_methods.models import Order, OrderItem, ProductCost, ProductCount


def get_top_order_by_sum_in_period(begin, end):
    """Возвращает заказ, который имеют наибольшую сумму за определенный промежуток времени
            Напишите функцию, которая выводит заказ с наибольшей общей суммой за период.
            Если несколько заказов имеют одинаковую сумму - вывести тот, чей номер больше.
    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает номер заказа и его сумму
    """

    order = Order.objects.filter(date_formation__range=[begin, end])
    __import__('pdb').set_trace()
    goods = OrderItem.objects.filter(
        
    )

    return result

from query_methods.models import OrderItem, ProductCost, ProductCount
from pprint import pprint
from django.db.models import Count, Sum, F, Q

def get_average_cost_without_product(product, begin, end):
    """Возвращает среднюю стоимость заказов без указанного товара за определенный промежуток времени

    Args:
        product: наименование товара
        begin: начало периода
        end: окончание периода

    Returns: возвращает числовое значение средней стоимости
    """

    order = OrderItem.objects.filter(
       order__date_formation__range=(
            begin,
            end
        )
    ).exclude(order__contains=filter(product__name=product))

    print(order)
    __import__('pdb').set_trace()
    
    
    return 

# .annotate(
#     staff_users=(
#         Count('id', filter=Q(is_staff=True))
#     ),
#     non_staff_users=(
#         Count('id', filter=Q(is_staff=False))
#     ),
# ))

    # goods = OrderItem.objects.filter(
    #     order__date_formation__range=[begin, end]
    # ).exclude(product__name=product)

    # product = {}
    # for item in goods:
    #     """ Формируем кол-во товара в наличии, только за текущий период """
    #     remaining_items_in_stock = ProductCount.objects.filter(
    #         begin__lte=item.order.date_formation,
    #         end__gte=item.order.date_formation,
    #         product__name=item.product.name).first()

    #     if remaining_items_in_stock:
    #         if remaining_items_in_stock.value < item.count:
    #             final_count_of_items = remaining_items_in_stock.value
    #         else:
    #             final_count_of_items = item.count
    #     """ Формируем цену cost, только если попадаем в период активной цены """
    #     cost = ProductCost.objects.filter(
    #         begin__lte=item.order.date_formation,
    #         end__gte=item.order.date_formation,
    #         product__name=item.product.name).first()

    #     if cost:
    #         if product.get(item.order.number):
    #             аmount = product[item.order.number] + cost.value * final_count_of_items
    #             product[item.order.number] = int(аmount)
    #         else:
    #             product[item.order.number] = int(cost.value * final_count_of_items)
    # pprint(product)
    # return int(sum(product.values())) / len(product) if product else 0

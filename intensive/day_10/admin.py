from django.contrib import admin

from .models import (Customer, Order, OrderItem, Product, ProductCost,
                     ProductCount)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


class ProductCountAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'begin', 'end', 'value')


class ProductCostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'begin', 'end', 'value')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'number', 'date_formation', 'customer')


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('pk', 'order', 'product', 'count')


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCount, ProductCountAdmin)
admin.site.register(ProductCost, ProductCostAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)

from django.contrib import admin

from .models import Product, ProductCost, ProductCount


class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    empty_value_display = '-пусто-'


class ProductCountAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'begin', 'end', 'value')
    empty_value_display = '-пусто-'


class ProductCostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'begin', 'end', 'value')
    empty_value_display = '-пусто-'


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCount, ProductCountAdmin)
admin.site.register(ProductCost, ProductCostAdmin)

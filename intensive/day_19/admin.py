from django.contrib import admin

from .models import Workers


class WorkersAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


admin.site.register(Workers, WorkersAdmin)
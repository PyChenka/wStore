from django.contrib import admin

from .models import *


class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    fk_name = 'order'
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'email',
        'time_create',
        'paid',
        'country',
    )
    list_filter = ('time_create', 'country', )
    fields = (
        'first_name',
        'last_name',
        'email',
        'postal_code',
        'country',
        'city',
        'address',
        'paid',
    )
    inlines = [OrderItemInLine, ]


admin.site.register(Order, OrderAdmin)
from django.urls import path

from orders.views import order_done, OrderCreate

app_name = 'orders'

urlpatterns = [
    path('create/', OrderCreate.as_view(), name='create_order'),
    path('done/', order_done, name='done')
    ]

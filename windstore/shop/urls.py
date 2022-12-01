from django.urls import path
from .views import ProductAll, show_single_product

app_name = 'shop'

urlpatterns = [
    path('', ProductAll.as_view(), name='index'),
    path('<slug:slug>/', show_single_product, name='single')
    ]

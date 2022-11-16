from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.show_all_products, name='index'),
    path('<slug:slug>/', views.show_single_product)
    ]

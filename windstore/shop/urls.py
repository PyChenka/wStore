from django.urls import path
from . import views
from .views import ProductAll

app_name = 'shop'

urlpatterns = [
    path('', ProductAll.as_view(), name='index'),
    path('<slug:slug>/', views.show_single_product, name='single')
    ]

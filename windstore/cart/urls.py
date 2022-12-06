from django.urls import path

from .views import cart_view, cart_add, cart_remove

app_name = 'cart'

urlpatterns = [
    path('', cart_view, name='index'),
    path('add/<slug:slug>/', cart_add, name='add'),
    path('remove/<slug:slug>/', cart_remove, name='remove'),
    ]
from django.urls import path

from mailings.views import SubscribeCreate, subscribe_done

app_name = 'subscribe'

urlpatterns = [
    path('', SubscribeCreate.as_view(), name='form'),
    path('done/', subscribe_done, name='done')
]
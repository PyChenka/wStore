from django.urls import path

from .views import SearchResult

app_name = 'search'

urlpatterns = [
    path('', SearchResult.as_view(), name='index'),
]
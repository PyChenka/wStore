from django.urls import path, re_path

from windstore.views import custom_404_view
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.show_all_articles, name='index'),
    re_path(r'^year/(?P<year>[0-9]{4})/', views.show_articles_by_year, name='by_year'),
    path('<slug:slug>/', views.show_single_article, name='single'),
    ]

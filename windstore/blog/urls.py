from django.urls import path, re_path

from .views import ArticleAll, ArticleByYear, show_single_article

app_name = 'blog'

urlpatterns = [
    path('', ArticleAll.as_view(), name='index'),
    re_path(r'^year/(?P<year>[0-9]{4})/', ArticleByYear.as_view(), name='by_year'),
    path('<slug:slug>/', show_single_article, name='single'),
    ]

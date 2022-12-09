from django.urls import path, re_path

from .views import ArticleAll, ArticleByYear, ArticleSingle

app_name = 'blog'

urlpatterns = [
    path('', ArticleAll.as_view(), name='index'),
    re_path(r'^year/(?P<year>[0-9]{4})/', ArticleByYear.as_view(), name='by_year'),
    path('<slug:slug>/', ArticleSingle.as_view(), name='single'),
    ]

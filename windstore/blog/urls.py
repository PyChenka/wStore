from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.show_all_posts, name='index'),
    path('<slug>/', views.show_post),
    ]

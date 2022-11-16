from django.http import HttpResponse
from django.shortcuts import render


def show_all_posts(request):
    return HttpResponse('Главная страница приложения BLOG, содержащая все посты с пагинацией')


def show_post(request, slug):
    return HttpResponse(f'Пост {slug}')
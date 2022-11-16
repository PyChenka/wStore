from django.http import HttpResponse
from django.shortcuts import render


def show_all_products(request):
    return HttpResponse('Главная страница приложения SHOP, содержит плитку из товаров')


def show_single_product(request, slug):
    return HttpResponse('Страница товара')
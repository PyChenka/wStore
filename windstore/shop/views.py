from django.http import HttpResponse
from django.shortcuts import render


def show_all_products(request):
    template = 'shop/catalog.html'
    return render(request, template)


def show_single_product(request, slug):
    return HttpResponse(f'Страница товара {slug}')
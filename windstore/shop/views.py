from django.http import HttpResponse
from django.shortcuts import render

from shop.models import Product


def show_all_products(request):
    template = 'shop/catalog.html'
    products = Product.objects.order_by('title')    # определить количество
    context = {
        'type': 'products',
        'title': 'Shop.',
        'objects': products,
    }
    return render(request, template, context)


def show_single_product(request, slug):
    template = 'shop/product.html'
    product = Product.objects.get(slug=slug)
    images = product.images.all()
    context = {
        'images': images,
        'product': product,
    }
    return render(request, template, context)
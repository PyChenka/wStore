from django.shortcuts import render
from shop.models import Product


def index(request):                                 # совпадает с show_all_products в shop/views
    template = 'index.html'
    products = Product.objects.order_by('title')    # определить количество
    context = {
        'type': 'products',
        'title': 'Shop products.',
        'objects': products,
    }
    return render(request, template, context)


def about(request):
    template = 'about.html'
    return render(request, template)


def contact(request):
    template = 'contact.html'
    return render(request, template)

from django.shortcuts import render

from shop.models import Product


def index(request):
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
    context = {'headline': ' - About'}
    return render(request, template, context)


def contact(request):
    template = 'contact.html'
    context = {'headline': ' - Contact'}
    return render(request, template, context)


def custom_error_view(request, exception=None):
    template = 'errors/custom_error.html'
    context = {'message': 'Что-то пошло не так :('}
    return render(request, template, context)


def custom_404_view(request, exception=None):
    template = 'errors/custom_error.html'
    context = {'message': 'Такой страницы не существует :('}
    return render(request, template, context)

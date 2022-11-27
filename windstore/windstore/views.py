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


def custom_error_view(request, exception=None):
    return render(request, "errors/custom_error.html", {'message': 'Что-то пошло не так :('})


def custom_404_view(request, exception=None):
    return render(request, "errors/custom_error.html", {'message': 'Такой страницы не существует :('})

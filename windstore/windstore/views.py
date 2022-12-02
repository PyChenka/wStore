from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView

from shop.models import Product

CONTEXT_MAIN = {
        'type': 'products',
        'title': 'Products.'
}


class MainPage(ListView):
    """Отображает главную страницу"""
    model = Product
    template_name = 'index.html'
    context_object_name = 'objects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(CONTEXT_MAIN)
        return context

    def get_queryset(self):
        return Product.objects.order_by('title')[:6]


@login_required
def about(request):
    template = 'about.html'
    context = {'headline': ' - About'}
    return render(request, template, context)


def custom_error_view(request, exception=None):
    template = 'errors/custom_error.html'
    context = {'message': 'Что-то пошло не так :('}
    return render(request, template, context)


def custom_404_view(request, exception=None):
    template = 'errors/custom_error.html'
    context = {'message': 'Такой страницы не существует :('}
    return render(request, template, context)

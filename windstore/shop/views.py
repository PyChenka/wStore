from django.shortcuts import render
from django.views.generic import ListView

from core.context_data import CONTEXT
from .models import Product


class ProductAll(ListView):
    """Отображает все товары, порядок: по названию"""
    model = Product
    template_name = 'catalog.html'
    context_object_name = 'objects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(CONTEXT['shop'])
        return context


def show_single_product(request, slug):
    """Отображает отдельный товар"""
    template = 'shop/product.html'
    product = Product.objects.get(slug=slug)
    images = product.images.all()
    review = product.reviews.filter(rating=5)[:1]
    CONTEXT['shop'].update({'product': product, 'images': images, 'reviews': review})
    return render(request, template, CONTEXT['shop'])

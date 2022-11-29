from django.shortcuts import render
from django.views.generic import ListView

from shop.models import Product


CONTEXT_SHOP = {
        'subtitle': ' - Shop',
        'type': 'products',
        'title': 'Shop.'
}


class ProductAll(ListView):
    """Отображает все товары, порядок: по названию"""
    model = Product
    template_name = 'catalog.html'
    context_object_name = 'objects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(CONTEXT_SHOP)
        return context


def show_single_product(request, slug):
    """Отображает отдельный товар"""
    template = 'shop/product.html'
    product = Product.objects.get(slug=slug)
    images = product.images.all()
    CONTEXT_SHOP.update({'product': product, 'images': images})
    return render(request, template, CONTEXT_SHOP)

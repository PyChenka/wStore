from django.shortcuts import render, redirect

from shop.models import Product
from .cart import Cart


def cart_add(request, slug):
    cart = Cart(request)
    product = Product.objects.get(slug=slug)
    cart.add_to_cart(product=product)
    return redirect('cart:index')


def cart_remove(request, slug):
    cart = Cart(request)
    product = Product.objects.get(slug=slug)
    cart.remove_from_cart(product=product)
    return redirect('cart:index')


def cart_view(request):
    cart = Cart(request)
    template = 'cart/cart.html'
    context = {'subtitle': ' - Cart', 'cart': cart}
    return render(request, template, context)

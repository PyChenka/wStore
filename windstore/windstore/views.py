from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from core.context_data import CONTEXT
from shop.models import Product, Review


class MainPage(ListView):
    """Отображает главную страницу"""
    model = Product
    template_name = 'index.html'
    context_object_name = 'objects'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(CONTEXT['main'])
        return context

    def get_queryset(self):
        return Product.objects.filter(available=True).order_by('title')


def about(request):
    template = 'about.html'
    context = CONTEXT['about']
    return render(request, template, context)


class Profile(LoginRequiredMixin, ListView):
    """Отображает личную страницу зарегистрированного пользователя"""
    model = Review
    template_name = 'profile.html'
    context_object_name = 'objects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                'subtitle': f' - {self.request.user.username}',
                'title': self.request.user.username
            }
        )
        return context

    def get_queryset(self):
        return self.request.user.reviews.select_related('product')


def custom_404_view(request, exception=None):
    template = 'errors/custom_error.html'
    context = {
        'message': 'Вы ищете что-то не то... :)'
    }
    return render(request, template, context)

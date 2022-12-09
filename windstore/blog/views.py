from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from core.context_data import CONTEXT
from .models import Article


class ArticleAll(ListView):
    """Отображает все статьи, порядок: по умолчанию"""
    model = Article
    template_name = 'catalog.html'
    context_object_name = 'objects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(CONTEXT['blog'])
        return context


class ArticleByYear(ListView):
    """Отображает статьи по годам, порядок: по умолчанию"""
    model = Article
    template_name = 'catalog.html'
    context_object_name = 'objects'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(CONTEXT['blog'])
        context['year'] = self.kwargs['year']
        return context

    def get_queryset(self):
        return Article.objects.filter(time_create__year=self.kwargs['year'])


@method_decorator(login_required, name='dispatch')
class ArticleSingle(DetailView):
    """Отображает отдельную статью"""
    model = Article
    template_name = 'blog/article.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(CONTEXT['blog'])
        return context

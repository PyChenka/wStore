from django.shortcuts import render
from django.views.generic import ListView

from blog.models import Article


CONTEXT_BLOG = {
        'subtitle': ' - Blog',
        'type': 'articles',
        'title': 'Articles.'
}


class ArticleAll(ListView):
    """Отображает все статьи, порядок: по умолчанию"""
    model = Article
    template_name = 'catalog.html'
    context_object_name = 'objects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(CONTEXT_BLOG)
        return context


class ArticleByYear(ListView):
    """Отображает статьи по годам, порядок: по умолчанию"""
    model = Article
    template_name = 'catalog.html'
    context_object_name = 'objects'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(CONTEXT_BLOG)
        context['year'] = self.kwargs['year']
        return context

    def get_queryset(self):
        return Article.objects.filter(time_create__year=self.kwargs['year']).order_by('-time_create')


def show_single_article(request, slug):
    """Отображает отдельную статью"""
    template = 'blog/article.html'
    article = Article.objects.get(time_create__date=slug)
    CONTEXT_BLOG.update({'article': article})
    return render(request, template, CONTEXT_BLOG)

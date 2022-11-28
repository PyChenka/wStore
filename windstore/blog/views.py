from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView

from blog.models import Article
from windstore.views import MENU


CONTEXT = {
        'menu': MENU,
        'name': 'Windstore',
        'headline': ' - Blog',
        'type': 'articles',
        'title': 'Articles.'
}


class ArticlesAll(ListView):
    model = Article
    template_name = 'catalog.html'
    context_object_name = 'objects'
    extra_context = CONTEXT

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Article.objects.all()


def show_all_articles(request):
    """Отображает все статьи, упорядоченные от самой новой"""
    template = 'catalog.html'
    articles = Article.objects.order_by('-time_create')
    context = CONTEXT
    context['objects'] = articles
    return render(request, template, context)


def show_single_article(request, slug):
    """Отображает отдельную статью"""
    template = 'blog/article.html'
    article = Article.objects.get(time_create__date=slug)
    context = CONTEXT
    context['article']: article
    return render(request, template, context)


def show_articles_by_year(request, year):
    """Отображает статьи по годам"""
    if int(year) < 2022:
        raise Http404()
    elif int(year) > 2023:
        return redirect('blog:index')

    template = 'catalog.html'
    articles = Article.objects.filter(time_create__year=year).order_by('-time_create')
    context = CONTEXT
    context['year']: year
    context['objects']: articles
    return render(request, template, context)

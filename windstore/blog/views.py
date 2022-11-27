from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

from blog.models import Article


def show_all_articles(request):
    """Отображает все статьи, упорядоченные от самой новой"""
    template = 'blog/articles.html'
    articles = Article.objects.order_by('-time_create')
    context = {
        'type': 'articles',
        'title': 'Articles.',
        'objects': articles,
    }
    return render(request, template, context)


def show_single_article(request, slug):
    """Отображает отдельную статью"""
    template = 'blog/article.html'
    article = Article.objects.get(time_create__date=slug)
    context = {
        'article': article,
    }
    return render(request, template, context)


def show_articles_by_year(request, year):
    """Отображает статьи по годам"""
    if int(year) < 2022:
        raise Http404()
    elif int(year) > 2023:
        return redirect('blog:index')

    template = 'blog/articles.html'
    articles = Article.objects.filter(time_create__year=year).order_by('-time_create')
    context = {
        'type': 'articles',
        'year': year,
        'title': 'Articles.',
        'objects': articles,
    }
    return render(request, template, context)

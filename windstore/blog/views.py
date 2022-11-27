from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

from blog.models import Article


def show_all_articles(request):
    template = 'blog/articles.html'
    articles = Article.objects.order_by('-time_create')
    context = {
        'type': 'articles',
        'title': 'Articles.',
        'objects': articles,
    }
    return render(request, template, context)


def show_single_article(request, slug):
    return HttpResponse(f'Пост {slug}')


def show_articles_by_year(request, year):
    if int(year) < 2022:
        raise Http404()
    elif int(year) > 2023:
        return redirect('blog:index')

    return HttpResponse(f'Статьи за {year} год')

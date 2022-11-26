from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Article


def show_all_posts(request):
    template = 'blog/articles.html'
    articles = Article.objects.order_by('-time_create')
    context = {
        'type': 'articles',
        'title': 'Articles.',
        'objects': articles,
    }
    return render(request, template, context)


def show_post(request, slug):
    return HttpResponse(f'Пост {slug}')
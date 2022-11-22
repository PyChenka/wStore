from django.http import HttpResponse
from django.shortcuts import render


def show_all_posts(request):
    template = 'blog/articles.html'
    return render(request, template)


def show_post(request, slug):
    return HttpResponse(f'Пост {slug}')
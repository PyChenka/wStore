from django.shortcuts import render


def index(request):
    template = 'index.html'
    return render(request, template)


def about(request):
    template = 'about.html'
    return render(request, template)


def contact(request):
    template = 'contact.html'
    return render(request, template)

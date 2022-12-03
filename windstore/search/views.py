from itertools import chain

from django.db.models import Q
from django.views.generic import ListView

from blog.models import Article
from shop.models import Product

CONTEXT_SEARCH = {
        'subtitle': ' - Search',
        'title': 'You searched'
}


class SearchResult(ListView):
    template_name = 'catalog.html'
    context_object_name = 'objects'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('q')
        context = super().get_context_data(**kwargs)
        context.update(CONTEXT_SEARCH)
        context.update({'text': query})
        return context

    def get_queryset(self):
        """Отбирает данные по поисковому запросу из двух моделей:
        Article и Product
        """
        queryset = []
        query = self.request.GET.get('q')
        if query:
            articles = Article.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
            products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
            queryset = list(chain(articles, products))
        print(queryset)
        return queryset



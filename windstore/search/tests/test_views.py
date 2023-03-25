import tempfile

from django.test import TestCase, Client
from django.urls import reverse

from blog.models import Article
from core.context_data import CONTEXT
from shop.models import Product


class SearchViewTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            title='Товар тест',  # slug : tovar
            main_image=tempfile.NamedTemporaryFile(suffix='.jpg').name,
            price=20.00,
        )
        self.article = Article.objects.create(
            title='Блог',  # slug : blog
            content='тест',
            image=tempfile.NamedTemporaryFile(suffix='.jpg').name
        )
        self.query = 'тест'

    def test_search_view_uses_correct_template(self):
        """По адресу страницы search:index загружается верный шаблон"""
        response = self.client.get(reverse('search:index'))
        self.assertTemplateUsed(response, 'catalog.html')

    def test_search_view_show_correct_context(self):
        """Шаблон страницы search:index сформирован с правильным текстовым контекстом"""
        response = self.client.get(reverse('search:index') + f'?q={self.query}')
        context_data = {response.context[key] for key in ('title', 'subtitle', 'text')}
        expected_context = {data for data in CONTEXT['search'].values()}
        expected_context.add(self.query)
        self.assertSetEqual(context_data, expected_context)

    def test_search_result_view_show_correct_context(self):
        """Шаблон страницы search:index сформирован с правильным набором данных"""
        response = self.client.get(reverse('search:index') + f'?q={self.query}')
        first_object = response.context['object_list'][0]
        second_object = response.context['object_list'][1]
        self.assertIn(first_object.title, ('Товар тест', 'Блог'))
        self.assertIn(second_object.title, ('Товар тест', 'Блог'))


class SearchPaginatorViewTest(TestCase):

    def setUp(self):
        for i in range(7):
            self.product = Product.objects.create(
                title=f'Result {i}',
                main_image=tempfile.NamedTemporaryFile(suffix='.jpg').name,
                price=20.00,
            )

    def test_first_page_contains_three_products(self):
        """Страница 1 отображает нужное количество объектов: 3"""
        response = self.client.get(reverse('search:index') + '?q=result')
        self.assertEqual(
            len(response.context['object_list']),
            6,
            msg='Количество товаров на первой странице не соответствует установленному в паджинаторе'
        )

    def test_second_page_contains_one_product(self):
        """Страница 2 отображает оставшиеся объекты: 1"""
        response = self.client.get(reverse('search:index') + '?q=result' + '&page=2')
        self.assertEqual(
            len(response.context['object_list']),
            1,
            msg='Количество товаров на второй странице не соответствует установленному в паджинаторе')

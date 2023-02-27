import tempfile

from django.test import TestCase, Client
from django.urls import reverse

from blog.models import Article
from core.context_data import CONTEXT


class BlogViewTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.article = Article.objects.create(
            title='Блог',  # slug : blog
            content='',
            image=tempfile.NamedTemporaryFile(suffix='.jpg').name
        )
        cls.pages = {
            reverse('blog:index'): 'catalog.html',
            reverse('blog:single', kwargs={'slug': 'blog'}): 'blog/article.html',
            reverse('blog:by_year', kwargs={'year': '2023'}): 'catalog.html',
        }

    def test_blog_views_use_correct_templates(self):
        """По адресам страниц blog:index, blog:single, blog:by_year загружаются верные шаблоны"""
        for reverse_name, temp in BlogViewTest.pages.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.client.get(reverse_name)
                self.assertTemplateUsed(response, temp)

    def test_blog_views_show_correct_context(self):
        """Шаблоны страниц сформированы с правильным текстовым контекстом"""
        for reverse_name, temp in BlogViewTest.pages.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.client.get(reverse_name)
                context_data = {response.context[key] for key in ('title', 'subtitle')}
                expected_context = {data for data in CONTEXT['blog'].values()}
                self.assertSetEqual(context_data, expected_context)

    def test_article_all_view_show_correct_context(self):
        """Шаблон страницы blog:index сформирован с правильным набором данных"""
        response = self.client.get(reverse('blog:index'))
        first_object = response.context['object_list'][0]
        article_title = first_object.title
        article_slug = first_object.slug
        self.assertEqual(article_title, 'Блог')
        self.assertEqual(article_slug, 'blog')

    def test_article_single_view_show_correct_context(self):
        """Шаблон страницы blog:single сформирован с правильным набором данных"""
        response = self.client.get(
            reverse(
                'blog:single',
                kwargs={'slug': 'blog'}
            )
        )
        self.assertEqual(response.context.get('article').title, 'Блог')
        self.assertEqual(response.context.get('article').slug, 'blog')

    def test_article_by_year_view_show_correct_context(self):
        """Шаблон страницы blog:by_year сформирован с правильным набором данных"""
        response = self.client.get(
            reverse(
                'blog:by_year',
                kwargs={'year': '2023'}
            )
        )
        first_object = response.context['object_list'][0]
        article_title = first_object.title
        article_slug = first_object.slug
        self.assertEqual(article_title, 'Блог')
        self.assertEqual(article_slug, 'blog')
        self.assertEqual(response.context.get('year'), '2023')




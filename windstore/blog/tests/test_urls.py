import tempfile
from http import HTTPStatus

from django.test import TestCase, Client

from blog.models import Article


class BlogURLTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.article = Article.objects.create(
            title='Привет',
            content='',
            image=tempfile.NamedTemporaryFile(suffix='.jpg').name
        )

    def test_blog_page_urls_exist(self):
        """Страницы /blog/<slug>/, /blog/year/<year>/ для неавторизованных пользователей доступны"""
        pages = (
            '/blog/privet/',
            '/blog/year/2023/',
        )
        for page in pages:
            with self.subTest(page=page):
                response = self.client.get(page)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_blog_page_urls_use_correct_templates(self):
        """По адресам страниц /blog/<slug>/, /blog/year/<year>/ загружаются верные шаблоны"""
        pages = {
            '/blog/privet/': 'blog/article.html',
            '/blog/year/2023/': 'catalog.html',
        }
        for page, temp in pages.items():
            with self.subTest(page=page):
                response = self.client.get(page)
                self.assertTemplateUsed(response, temp)


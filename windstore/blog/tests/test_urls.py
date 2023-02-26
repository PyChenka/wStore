import tempfile
from http import HTTPStatus

from django.test import TestCase, Client

from blog.models import Article


class BlogURLTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.article = Article.objects.create(
            title='Блаблабла',
            content='',
            image=tempfile.NamedTemporaryFile(suffix='.jpg').name
        )

    def setUp(self):
        self.guest_client = Client()

    def test_blog_page_urls_exist(self):
        """Страницы /blog/<slug>/, /blog/year/<year>/ для неавторизованных пользователей доступны"""
        pages = (
            '/blog/blablabla/',
            '/blog/year/2023/',
        )
        for page in pages:
            with self.subTest(page=page):
                response = self.guest_client.get(page)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_common_page_urls_use_correct_template(self):
        """По адресам страниц /blog/<slug>/, /blog/year/<year>/ загружаются верные шаблоны"""
        pages = {
            '/blog/blablabla/': 'blog/article.html',
            '/blog/year/2023/': 'catalog.html',
        }
        for page, temp in pages.items():
            with self.subTest(page=page):
                response = self.guest_client.get(page)
                self.assertTemplateUsed(response, temp)


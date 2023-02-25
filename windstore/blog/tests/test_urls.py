import tempfile

from django.test import TestCase, Client

from blog.models import Article


class BlogURLTests(TestCase):

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

    def test_blog_single_article_url_exists(self):
        """Страница /blog/<slug>/ отдельной статьи доступна"""
        response = self.client.get('/blog/blablabla/')
        self.assertEqual(response.status_code, 200)
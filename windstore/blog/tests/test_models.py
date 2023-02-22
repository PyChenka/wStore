from django.test import TestCase

from blog.models import Article


class ArticleModelTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.article = Article.objects.create(
            title='Тест'*10,
            content='',
            image=None
        )

    def test_object_name_is_title_field(self):
        """Строковое представление совпадает с полем title"""
        article = ArticleModelTests.article
        expected_object_name = article.title
        self.assertEqual(expected_object_name, str(article), msg='Неверное строковое представление.')

    def test_title_convert_to_slug(self):
        """Содержимое поля title правильно конвертируется в slug"""
        article = ArticleModelTests.article
        slug = article.slug
        self.assertEqual(slug, 'test'*10)

    def test_slug_less_than_max_length(self):
        """Созданный slug не превышает max_length"""
        article = ArticleModelTests.article
        slug_max_length = article._meta.get_field('slug').max_length
        slug_length = len(article.slug)
        self.assertLessEqual(slug_length, slug_max_length)

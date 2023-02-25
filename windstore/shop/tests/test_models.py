import os
import tempfile

from django.contrib.auth.models import User
from django.test import TestCase

from shop.models import Product, Gallery, Review, get_upload_path


class ProductModelTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product = Product.objects.create(
            title='Тест'*10,
            main_image=tempfile.NamedTemporaryFile(suffix='.jpg').name,
            price=100.0,
        )

    def test_object_name_is_title_field(self):
        """Строковое представление совпадает с полем title'"""
        product = ProductModelTests.product
        expected_object_name = product.title
        self.assertEqual(expected_object_name, str(product), msg='Неверное строковое представление.')

    def test_url_based_from_slug(self):
        """Формируется ссылка на объект на основе slug"""
        product = ProductModelTests.product
        response = self.client.post(product.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_title_convert_to_slug(self):
        """Содержимое поля title правильно конвертируется в slug"""
        product = ProductModelTests.product
        slug = product.slug
        self.assertEqual(slug, 'test'*10)

    def test_slug_less_than_max_length(self):
        """Созданный slug не превышает max_length"""
        product = ProductModelTests.product
        slug_max_length = product._meta.get_field('slug').max_length
        slug_length = len(product.slug)
        self.assertLessEqual(slug_length, slug_max_length)


class ReviewModelTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product = Product.objects.create(
            title='Тест'*10,
            main_image=tempfile.NamedTemporaryFile(suffix='.jpg').name,
            price=100.0,
        )
        cls.user = User.objects.create_user(
            username='Пользователь'
        )
        cls.review = Review.objects.create(
            product=cls.product,
            customer=cls.user,
            name='Имя',
            rating=5,
        )

    def test_object_name_includes_date_published(self):
        """Строковое представление имеет вид: 'Name: date_published'"""
        review = ReviewModelTests.review
        expected_object_name = f'{review.name}: {review.date_published}'
        self.assertEqual(expected_object_name, str(review), msg='Неверное строковое представление.')


class UtilsTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.file = tempfile.NamedTemporaryFile(suffix='.jpg').name
        cls.product = Product.objects.create(
            title='Тест',
            main_image=cls.file,
            price=100.0,
        )
        cls.gallery = Gallery.objects.create(
            image=cls.file,
            product=cls.product,
        )

    def test_correct_upload_path(self):
        """Формируется верный путь для загрузки изображения"""
        file = os.path.basename(self.file)
        expected_path = f'shop\\images\\test\\{file}'
        self.assertEqual(expected_path, get_upload_path(self.product, file))
        self.assertEqual(expected_path, get_upload_path(self.gallery, file))

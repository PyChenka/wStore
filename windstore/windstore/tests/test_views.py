import tempfile

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from shop.models import Product, Review

User = get_user_model()


class MainViewTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product = Product.objects.create(
            title='Товар тест',  # slug : tovar-test
            main_image=tempfile.NamedTemporaryFile(suffix='.jpg').name,
            price=20.00,
        )

    def test_main_about_views_use_correct_templates(self):
        """По адресам страниц main, about загружаются верные шаблоны"""
        pages = {
            reverse('main'): 'index.html',
            reverse('about'): 'about.html',
        }
        for reverse_name, temp in pages.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.client.get(reverse_name)
                self.assertTemplateUsed(response, temp)

    def test_main_view_show_correct_context(self):
        """Шаблон страницы main сформирован с правильным набором данных"""
        response = self.client.get(reverse('main'))
        first_object = response.context['object_list'][0]
        product_title = first_object.title
        product_slug = first_object.slug
        product_price = first_object.price
        self.assertEqual(product_title, 'Товар тест')
        self.assertEqual(product_slug, 'tovar-test')
        self.assertEqual(product_price, 20.00)
        self.assertEqual(response.context.get('title'), 'Products.')

    def test_about_view_show_correct_context(self):
        """Шаблон страницы about сформирован с правильным текстовым контекстом"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.context.get('subtitle'), ' - About')


class ProfileViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='auth')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

        self.product = Product.objects.create(
            title='Товар',  # slug : tovar
            main_image=tempfile.NamedTemporaryFile(suffix='.jpg').name,
            price=20.00,
        )
        self.review = Review.objects.create(
            product=self.product,
            customer=self.user,
            name='Имя',
            rating=5,
        )

    def test_profile_view_uses_correct_template_authorized(self):
        """По адресу страницы profile загружается верный шаблон"""
        response = self.authorized_client.get(reverse('profile'))
        self.assertTemplateUsed(response, 'profile.html')

    def test_profile_view_show_correct_context_authorized(self):
        """Шаблон страницы profile сформирован с правильным набором данных"""
        response = self.authorized_client.get(reverse('profile'))
        first_object = response.context['object_list'][0]
        review_product_title = first_object.product.title
        review_product_rating = first_object.rating
        self.assertEqual(review_product_title, 'Товар')
        self.assertEqual(review_product_rating, 5)
        self.assertEqual(response.context.get('title'), 'auth')
        self.assertEqual(response.context.get('subtitle'), ' - auth')


class MainPaginatorViewTest(TestCase):

    def setUp(self):
        for i in range(7):
            self.product = Product.objects.create(
                title=f'Товар {i}',
                main_image=tempfile.NamedTemporaryFile(suffix='.jpg').name,
                price=20.00,
            )

    def test_first_page_contains_six_products(self):
        """Страница 1 отображает нужное количество товаров: 6"""
        response = self.client.get(reverse('main'))
        self.assertEqual(
            len(response.context['object_list']),
            6,
            msg='Количество товаров на первой странице не соответствует установленному в паджинаторе'
        )

    def test_second_page_contains_one_product(self):
        """Страница 2 отображает оставшийся 1 товар"""
        response = self.client.get(reverse('main') + '?page=2')
        self.assertEqual(
            len(response.context['object_list']),
            1,
            msg='Количество товаров на второй странице не соответствует установленному в паджинаторе')


class ErrorViewTest(TestCase):

    def test_custom_404_view_uses_correct_template(self):
        """По адресам страниц ошибки 404 загружается кастомный шаблон"""
        response = self.client.get('/non-existent-page/')
        self.assertTemplateUsed(response, 'errors/custom_error.html')

    def test_custom_404_view_shows_correct_context(self):
        """Шаблон страницы ошибки 404 сформирован с правильным текстовым контекстом"""
        response = self.client.get('/non-existent-page/')
        self.assertEqual(response.context.get('message'), "You're looking for something wrong... :)")






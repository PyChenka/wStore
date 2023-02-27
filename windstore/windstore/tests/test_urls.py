from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase, Client

User = get_user_model()


class CommonPagesURLTest(TestCase):

    def setUp(self):
        self.pages = {
            '/': 'index.html',
            '/shop/': 'catalog.html',
            '/blog/': 'catalog.html',
            '/contact/': 'contact/contact.html',
            '/search/': 'catalog.html',
            '/cart/': 'cart/cart.html',
        }

    def test_common_pages_urls_exist(self):
        """Основные страницы для неавторизованных пользователей доступны"""
        for page in self.pages.keys():
            with self.subTest(page=page):
                response = self.client.get(page)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_common_pages_urls_use_correct_templates(self):
        """По адресам основных страниц загружаются верные шаблоны"""
        for page, temp in self.pages.items():
            with self.subTest(page=page):
                response = self.client.get(page)
                self.assertTemplateUsed(response, temp)


class ProfilePageURLTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='auth')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_profile_url_redirect_anonymous(self):
        """Страница /profile/ перенаправляет неавторизованного пользователя"""
        response = self.client.get('/profile/')
        self.assertRedirects(response, '/auth/login/?next=/profile/')

    def test_profile_url_authorized_client(self):
        """Страница /profile/ доступна для авторизованного пользователя"""
        response = self.authorized_client.get('/profile/')
        self.assertEqual(response.status_code, HTTPStatus.OK)


class AboutPageURLTest(TestCase):

    def test_about_url_exists(self):
        """Страница /about/ доступна"""
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_about_url_uses_correct_template(self):
        """По адресу /about/ загружается верный шаблон"""
        response = self.client.get('/about/')
        self.assertTemplateUsed(response, 'about.html')

from http import HTTPStatus

from django.test import TestCase, Client


class CommonPageURLTest(TestCase):

    def setUp(self):
        self.guest_client = Client()
        self.pages = {
            '/': 'index.html',
            '/shop/': 'catalog.html',
            '/blog/': 'catalog.html',
            '/contact/': 'contact/contact.html',
            '/search/': 'catalog.html',
            '/cart/': 'cart/cart.html',
        }

    def test_common_page_urls_exist(self):
        """Основные страницы для неавторизованных пользователей доступны"""
        for page in self.pages.keys():
            with self.subTest(page=page):
                response = self.guest_client.get(page)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_common_page_urls_use_correct_templates(self):
        """По адресам основных страниц загружаются верные шаблоны"""
        for page, temp in self.pages.items():
            with self.subTest(page=page):
                response = self.guest_client.get(page)
                self.assertTemplateUsed(response, temp)

    def test_profile_url_redirect_anonymous(self):
        """Страница /profile/ перенаправляет неавторизованного пользователя"""
        response = self.guest_client.get('/profile/')
        self.assertRedirects(response, '/auth/login/?next=/profile/')


class StaticPageURLTest(TestCase):

    def setUp(self):
        self.guest_client = Client()

    def test_about_url_exists(self):
        """Страница /about/ доступна"""
        response = self.guest_client.get('/about/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_about_url_uses_correct_template(self):
        """По адресу /about/ загружается верный шаблон"""
        response = self.guest_client.get('/about/')
        self.assertTemplateUsed(response, 'about.html')

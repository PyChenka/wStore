from http import HTTPStatus

from django.test import TestCase, Client


class PageURLTest(TestCase):

    def setUp(self):
        self.guest_client = Client()

    def test_common_page_urls_exist(self):
        """Основные страницы для неавторизованных пользователей доступны"""
        pages = (
            '/',
            '/shop/',
            '/blog/',
            '/contact/',
            '/search/',
            '/cart/',
        )
        for page in pages:
            with self.subTest(page=page):
                response = self.guest_client.get(page)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_common_page_urls_use_correct_templates(self):
        """По адресам основных страниц загружаются верные шаблоны"""
        page_temp = {
            '/': 'index.html',
            '/shop/': 'catalog.html',
            '/blog/': 'catalog.html',
            '/contact/': 'contact/contact.html',
            '/search/': 'catalog.html',
            '/cart/': 'cart/cart.html',
        }
        for page, temp in page_temp.items():
            with self.subTest(page=page):
                response = self.guest_client.get(page)
                self.assertTemplateUsed(response, temp)

    def test_profile_url_redirect_anonymous(self):
        """Страница /profile/ перенаправляет неавторизованного пользователя"""
        response = self.guest_client.get('/profile/')
        self.assertEqual(response.status_code, HTTPStatus.FOUND)


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


class DonePageURLTest(TestCase):

    def setUp(self):
        self.guest_client = Client()
        self.pages = (
            '/contact/done/',
            '/search/done/',
            '/orders/done/',
            '/subscribe/done/',
        )

    def test_done_page_urls_exist(self):
        """Страницы подтверждения /contact/done/, /search/done/, /orders/done/, /subscribe/done/ доступны"""
        for page in self.pages:
            with self.subTest(page=page):
                response = self.guest_client.get(page)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    # def test_done_page_urls_use_correct_templates(self):
    #     """По адресам /contact/done/, /search/done/, /orders/done/, /subscribe/done/ загружаются верные шаблоны"""
    #     for page in self.pages:
    #         with self.subTest(page=page):
    #             response = self.guest_client.get(page)
    #             self.assertTemplateUsed(response, 'done_message.html')
from django.test import TestCase, Client


class PageURLTests(TestCase):

    def setUp(self):
        self.guest_client = Client()

    def test_common_page_urls_exist(self):
        """
        Адреса основных страниц
        для неавторизованных пользователей
        доступны
        """
        pages = ('/',
                 '/shop/',
                 '/blog/',
                 '/contact/',
                 '/search/',
                 '/cart/',
                 )
        for page in pages:
            with self.subTest(page=page):
                response = self.guest_client.get(page)
                self.assertEqual(response.status_code, 200)

    def test_profile_url_redirect_anonymous(self):
        """
        Страница /profile/ перенаправляет
        неавторизованного пользователя
        """
        response = self.guest_client.get('/profile/')
        self.assertEqual(response.status_code, 302)


class StaticPageURLTests(TestCase):

    def setUp(self):
        self.guest_client = Client()

    def test_about_url_exists(self):
        """Адрес /about/ доступен"""
        response = self.guest_client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_about_url_uses_correct_template(self):
        """По адресу /about/ загружается верный шаблон"""
        response = self.guest_client.get('/about/')
        self.assertTemplateUsed(response, 'about.html')






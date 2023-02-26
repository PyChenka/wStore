from http import HTTPStatus

from django.test import TestCase, Client


class OrderURLTest(TestCase):

    def setUp(self):
        self.guest_client = Client()

    def test_order_create_url_exists(self):
        """Страница /orders/create/ доступна"""
        response = self.guest_client.get('/orders/create/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_order_create_url_uses_correct_template(self):
        """По адресу /orders/create/ загружается верный шаблон"""
        response = self.guest_client.get('/orders/create/')
        self.assertTemplateUsed(response, 'orders/order.html')

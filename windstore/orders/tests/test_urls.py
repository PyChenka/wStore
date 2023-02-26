from http import HTTPStatus

from django.test import TestCase, Client


class OrdersURLTest(TestCase):

    def setUp(self):
        self.guest_client = Client()

    def test_orders_create_url_exists(self):
        """Страница создания заказа /orders/create/ доступна"""
        response = self.guest_client.get('/orders/create/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_orders_create_url_uses_correct_template(self):
        """По адресу /orders/create/ загружается верный шаблон"""
        response = self.guest_client.get('/orders/create/')
        self.assertTemplateUsed(response, 'orders/order.html')

    def test_orders_done_url_exists(self):
        """Страница подтверждения заказа /orders/done/ доступна"""
        response = self.guest_client.get('/orders/done/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_orders_done_url_uses_correct_template(self):
        """По адресу /orders/done/ загружается верный шаблон"""
        response = self.guest_client.get('/orders/done/')
        self.assertTemplateUsed(response, 'done_message.html')

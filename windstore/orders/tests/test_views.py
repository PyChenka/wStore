from django.test import TestCase, Client
from django.urls import reverse


class OrdersViewTest(TestCase):

    def test_orders_views_use_correct_templates(self):
        """По адресам страниц orders:create_order, orders:done загружаются верные шаблоны"""
        pages = {
            reverse('orders:create_order'): 'orders/order.html',
            reverse('orders:done'): 'done_message.html',
        }
        for reverse_name, temp in pages.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.client.get(reverse_name)
                self.assertTemplateUsed(response, temp)

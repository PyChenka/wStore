from django.test import TestCase
from django.urls import reverse

from orders.models import Order


class OrderFormTest(TestCase):

    def test_create_order(self):
        """Валидная форма создает запись в Order"""
        orders_count = Order.objects.count()
        form_data = {
            'first_name': 'testName',
            'last_name': '000',
            'email': '1@mail.ru',
            'postal_code': '000000',
            'country': 'US',
            'city': '1',
            'address': '1'
        }
        response = self.client.post(
            reverse('orders:create_order'),
            data=form_data,
            follow=True
        )
        self.assertRedirects(response, reverse('orders:done'))
        self.assertEqual(Order.objects.count(), orders_count + 1)
        self.assertTrue(
            Order.objects.filter(
                first_name='testName',
            ).exists()
        )
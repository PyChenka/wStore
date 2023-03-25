import tempfile
from http import HTTPStatus

from django.test import TestCase, Client
from django.urls import reverse

from cart.cart import Cart
from shop.models import Product


class RequestFactory:
    pass


class CartViewTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product = Product.objects.create(
            title='Товар корзина',  # slug : tovar-korzina
            main_image=tempfile.NamedTemporaryFile(suffix='.jpg').name,
            price=20.00,
        )

    def test_cart_index_view_uses_correct_template(self):
        """По адресу страницы cart:index загружается верный шаблон"""
        response = self.client.get(reverse('cart:index'))
        self.assertTemplateUsed(response, 'cart/cart.html')

    def test_cart_add_remove_views_redirect_successful(self):
        """По адресу страниц cart:add, cart:remove происходит перенаправление"""
        pages = (
            reverse('cart:add', kwargs={'slug': 'tovar-korzina'}),
            reverse('cart:remove', kwargs={'slug': 'tovar-korzina'})
        )
        for page in pages:
            with self.subTest(page=page):
                response = self.client.get(page)
                self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_cart_index_view_show_correct_context(self):
        """Шаблон страницы cart:index сформирован с правильным контекстом"""
        response = self.client.get(reverse('cart:index'))
        self.assertEqual(response.context.get('subtitle'), ' - Cart')

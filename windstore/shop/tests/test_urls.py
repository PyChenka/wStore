import tempfile
from http import HTTPStatus

from django.test import TestCase, Client

from shop.models import Product


class ShopURLTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product = Product.objects.create(
            title='Товар тест',
            main_image=tempfile.NamedTemporaryFile(suffix='.jpg').name,
            price=50.00,
        )

    def setUp(self):
        self.guest_client = Client()

    def test_shop_single_product_url_exists(self):
        """Страница /shop/<slug>/ отдельного товара доступна"""
        response = self.guest_client.get('/shop/tovar-test/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_shop_single_product_url_uses_correct_template(self):
        """По адресу /shop/<slug>/ загружается верный шаблон"""
        response = self.guest_client.get('/shop/tovar-test/')
        self.assertTemplateUsed(response, 'shop/product.html')

import tempfile

from django.test import TestCase, Client

from shop.models import Product


class ShopURLTests(TestCase):

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
        response = self.client.get('/shop/tovar-test/')
        self.assertEqual(response.status_code, 200)
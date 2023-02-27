import tempfile

from django.test import TestCase, Client

from shop.models import Product


class CartURLTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product = Product.objects.create(
            title='Товар в корзину',  # tovar-v-korzinu
            main_image=tempfile.NamedTemporaryFile(suffix='.jpg').name,
            price=60.00,
        )

    def test_cart_add_url_redirect_successful(self):
        """Страница /cart/add/<slug>/ добавления товара перенаправляет успешно"""
        response = self.client.get('/cart/add/tovar-v-korzinu/')
        self.assertRedirects(response, '/cart/')

    def test_cart_remove_url_redirect_successful(self):
        """Страница /cart/remove/<slug>/ удаления товара перенаправляет успешно"""
        response = self.client.get('/cart/remove/tovar-v-korzinu/')
        self.assertRedirects(response, '/cart/')

import tempfile
from decimal import Decimal
from unittest import mock

from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase, RequestFactory

from cart.cart import Cart
from shop.models import Product


class CartTest(TestCase):

    def setUp(self):
        self.request = RequestFactory().get('/')
        get_response = mock.MagicMock()
        middleware = SessionMiddleware(get_response)
        middleware.process_request(self.request)
        self.request.session['cart'] = {
            'star-tovar': {
                'quantity': 1,
                'price': '10.0'
            },
            'prosto-tovar': {
                'quantity': 2,
                'price': '20.0'
            }
        }
        self.request.session.save()

        self.cart = Cart(self.request)

        self.existing_product = Product.objects.create(
            title='Стар товар',  # slug : star-tovar
            main_image=tempfile.NamedTemporaryFile(suffix='.jpg').name,
            price=10.0,
        )
        self.new_product = Product.objects.create(
            title='Нов товар',  # slug : nov-tovar
            main_image=tempfile.NamedTemporaryFile(suffix='.jpg').name,
            price=30.0,
        )
        self.just_product = Product.objects.create(
            title='Просто товар',  # slug : prosto-tovar
            main_image=tempfile.NamedTemporaryFile(suffix='.jpg').name,
            price=20.0,
        )

    def test_adding_new_product_to_cart_successful(self):
        """Новый товар успешно добавляется в корзину"""
        self.cart.add_to_cart(product=self.new_product)
        expected_cart = {
            'star-tovar': {
                'quantity': 1,
                'price': '10.0'
            },
            'prosto-tovar': {
                'quantity': 2,
                'price': '20.0'
            },
            'nov-tovar': {
                'quantity': 1,
                'price': '30.0'
            }
        }
        self.assertEqual(self.cart.cart, expected_cart)

    def test_adding_existing_product_to_cart_successful(self):
        """Количество товара в корзине увеличивается при добавлении того же товара"""
        self.cart.add_to_cart(product=self.existing_product)
        expected_cart = {
            'star-tovar': {
                'quantity': 2,
                'price': '10.0'
            },
            'prosto-tovar': {
                'quantity': 2,
                'price': '20.0'
            },
        }
        self.assertEqual(self.cart.cart, expected_cart)

    def test_removing_existing_product_from_cart_successful(self):
        """Удаляется товар из корзины"""
        self.cart.remove_from_cart(product=self.existing_product)
        expected_cart = {
            'prosto-tovar': {
                'quantity': 2,
                'price': '20.0'
            }
        }
        self.assertEqual(self.cart.cart, expected_cart)

    def test_cart_iter_returns_products_successful(self):
        """Перебираются товары в корзине, извлекаются данные о товаре из БД"""
        product_list = []
        for prod in self.cart:
            product_list.append(prod)
        expected_list = [
            {
                'quantity': 1,
                'price': Decimal('10.0'),
                'product': self.existing_product,
                'total_price': Decimal('10.0')
            },
            {
                'quantity': 2,
                'price': Decimal('20.0'),
                'product': self.just_product,
                'total_price': Decimal('40.0')
            }
        ]
        self.assertListEqual(product_list, expected_list)

    def test_cart_len_counts_products_successful(self):
        """Верно считается общее количество товаров в корзине"""
        self.assertEqual(len(self.cart), 3)

    def test_cart_total_price_counts_successful(self):
        """Верно считается общая стоимость товаров в корзине"""
        self.assertEqual(self.cart.get_total_cart_price(), 50.0)

    def test_cart_fix_remove_deleted_product_succesful(self):
        """При удалении товара из БД он удаляется из корзины"""
        self.just_product.delete()
        self.cart.fix_cart()
        expected_cart = {
            'star-tovar': {
                'quantity': 1,
                'price': '10.0'
            }
        }
        self.assertEqual(self.cart.cart, expected_cart)

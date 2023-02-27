import tempfile

from django.test import TestCase, Client
from django.urls import reverse

from shop.models import Product


class ShopViewTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product = Product.objects.create(
            title='Товар тест',  # slug : tovar-test
            main_image=tempfile.NamedTemporaryFile(suffix='.jpg').name,
            price=20.00,
        )

    def test_shop_views_use_correct_templates(self):
        """По адресам страниц shop:index, shop:single загружаются верные шаблоны"""
        pages = {
            reverse('shop:index'): 'catalog.html',
            reverse('shop:single', kwargs={'slug': 'tovar-test'}): 'shop/product.html',
        }
        for reverse_name, temp in pages.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.client.get(reverse_name)
                self.assertTemplateUsed(response, temp)

    def test_product_all_view_show_correct_context(self):
        """Шаблон страницы shop:index сформирован с правильным набором данных"""
        response = self.client.get(reverse('shop:index'))
        first_object = response.context['object_list'][0]
        product_title = first_object.title
        product_slug = first_object.slug
        product_price = first_object.price
        self.assertEqual(product_title, 'Товар тест')
        self.assertEqual(product_slug, 'tovar-test')
        self.assertEqual(product_price, 20.00)

    def test_product_single_view_show_correct_context(self):
        """Шаблон страницы shop:single сформирован с правильным набором данных"""
        response = self.client.get(
            reverse(
                'shop:single',
                kwargs={'slug': 'tovar-test'}
            )
        )
        self.assertEqual(response.context.get('product').title, 'Товар тест')
        self.assertEqual(response.context.get('product').slug, 'tovar-test')
        self.assertEqual(response.context.get('product').price, 20.00)
        self.assertEqual(response.context.get('title'), 'Shop.')
        self.assertEqual(response.context.get('subtitle'), ' - Shop')


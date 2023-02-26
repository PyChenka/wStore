from django.test import TestCase

from orders.models import Order, OrderItem


class OrderModelTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.order = Order.objects.create(
            first_name='Тест'*10,
        )

    def test_object_name_includes_order_time_create(self):
        """Строковое представление имеет вид: 'Order: time_create'"""
        order = OrderModelTest.order
        expected_object_name = f'Order {order.time_create}'
        self.assertEqual(expected_object_name, str(order), msg='Неверное строковое представление.')


class OrderItemModelTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.order = Order.objects.create(
            first_name='Тест'*10,
        )
        cls.item = OrderItem.objects.create(
            order=cls.order,
            price=100.0,
            quantity=2,
        )

    def test_object_name_is_pk_field(self):
        """Строковое представление совпадает с полем pk"""
        item = OrderItemModelTest.item
        expected_object_name = str(item.pk)
        self.assertEqual(expected_object_name, str(item), msg='Неверное строковое представление.')

    def test_item_cost_calculation(self):
        """
        Общая сумма по товару в заказе вычисляется по формуле:
        цена товара * количество штук
        """
        item = OrderItemModelTest.item
        cost = item.get_cost()
        self.assertEqual(cost, 200.0)
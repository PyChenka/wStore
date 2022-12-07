from django.db import models
from shop.models import Product
from core.choice_settings import ORDERS_COUNTRIES


class Order(models.Model):
    """Сведения о заказе"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    postal_code = models.CharField(max_length=50)
    country = models.CharField(max_length=20, choices=ORDERS_COUNTRIES)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['-time_create']

    def __str__(self):
        return f'Order {self.time_create}'

    def get_total_price(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    """Отдельный товар в заказе"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='order_items')
    price = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.pk)

    def get_cost(self):
        return self.price * self.quantity

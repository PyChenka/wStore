from django.forms import ModelForm
from .models import Order


class OrderCreateForm(ModelForm):
    """Форма для ввода сведений о заказе"""
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'postal_code', 'country', 'city', 'address')

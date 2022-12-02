from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    """Форма обратной связи для страницы Contact"""
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'message')

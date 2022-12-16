from django.forms import ModelForm, TextInput
from .models import MailingList


class SubscribeForm(ModelForm):
    """Форма подписки на email рассылку"""
    class Meta:
        model = MailingList
        fields = ('email', )
        widgets = {
            'email': TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Enter your email'}),
        }
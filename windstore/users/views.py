from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import CreationForm


class SignUp(CreateView):
    """Отображает страницу регистрации"""
    form_class = CreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('main')


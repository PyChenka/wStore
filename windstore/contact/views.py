from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ContactForm
from .models import Contact


class ContactCreate(CreateView):
    """Отображает страницу с формой обратной связи"""
    model = Contact
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'subtitle': ' - Contact'})
        return context

    def get_initial(self):
        if self.request.user.is_authenticated:
            return {
                'first_name': self.request.user.first_name,
                'last_name': self.request.user.last_name,
                'email': self.request.user.email
            }

    def form_valid(self, form):
        """Отправляет сообщение с данными из формы"""
        data = form.data
        send_mail(f'Новое сообщение', data['message'], data['email'], ['my@mail.com'])
        return super().form_valid(form)


def contact_done(request):
    """Отображает страницу подтверждения после успешной отправки формы"""
    template = 'done_message.html'
    context = {
        'subtitle': ' - Contact',
        'msg': 'Your message has been sent!'
    }
    return render(request, template, context)





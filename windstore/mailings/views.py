from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import MailingList
from .forms import SubscribeForm
from .services import add_to_unisender_common_list


class SubscribeCreate(CreateView):
    """Отображает форму подписки на email рассылку"""
    model = MailingList
    form_class = SubscribeForm
    success_url = reverse_lazy('subscribe:done')

    def form_valid(self, form):
        """Проверяет наличие адреса почты в БД"""
        data = form.cleaned_data['email']
        if MailingList.objects.filter(email__iexact=data).exists():
            return render(self.request, 'errors/custom_error.html',
                          {'message': 'This address is already registered in the mailing list. Try another one.'})
        form.save()
        add_to_unisender_common_list(data)
        return super().form_valid(form)


def subscribe_done(request):
    """Отображает страницу подтверждения после успешной подписки"""
    template = 'done_message.html'
    context = {
        'subtitle': ' - Subscribe',
        'msg': 'The subscription has been issued successfully!'
    }
    return render(request, template, context)

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem, Order


class OrderCreate(CreateView):
    """Отображает страницу с формой для ввода сведений о заказе"""
    model = Order
    template_name = 'orders/order.html'
    form_class = OrderCreateForm
    success_url = reverse_lazy('orders:done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(self.request)
        context.update({'subtitle': ' - Order',
                        'cart': cart})
        return context

    def get_initial(self):
        if self.request.user.is_authenticated:
            return {
                'first_name': self.request.user.first_name,
                'last_name': self.request.user.last_name,
                'email': self.request.user.email
            }

    def form_valid(self, form):
        """Формирует заказ и очищает корзину"""
        if self.request.user.is_authenticated:
            order = form.save(commit=False)
            order.customer = self.request.user
        order = form.save()
        cart = Cart(self.request)
        for item in cart:
            OrderItem.objects.create(order=order,
                                     product=item['product'],
                                     price=item['price'],
                                     quantity=item['quantity'])
        cart.clear_cart()
        return super().form_valid(form)


def order_done(request):
    """Отображает страницу подтверждения после успешной отправки формы"""
    template = 'done_message.html'
    context = {
        'subtitle': ' - Order',
        'msg': 'Thank you for your order!'
    }
    return render(request, template, context)
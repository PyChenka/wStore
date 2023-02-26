from decimal import Decimal

from shop.models import Product
from windstore.settings import CART_SESSION_ID


class Cart:
    """Управляет корзиной покупок"""

    def __init__(self, request):
        """Инициализирует корзину (пустую, если корзина отсутствует в сессии)"""
        self.session = request.session
        if CART_SESSION_ID not in self.session:
            self.session[CART_SESSION_ID] = {}
        self.cart = self.session.get(CART_SESSION_ID)

    def add_to_cart(self, product: Product):
        """Добавляет товар в корзину или обновляет его количество. Идентификация по слагу"""
        product_id = product.slug
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        self.cart[product_id]['quantity'] += 1
        self.save()

    def remove_from_cart(self, product: Product):
        """Удаляет товар из корзины. Идентификация по слагу"""
        product_id = product.slug
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        """Обновляет корзину в сессии"""
        self.session[CART_SESSION_ID] = self.cart
        self.session.modified = True

    def __iter__(self):
        """Перебирает элементы в корзине и получает товары из БД"""
        products = Product.objects.filter(slug__in=self.cart.keys())
        for product in products:
            self.cart[product.slug]['product'] = product

        for prod in self.cart.values():
            prod['price'] = Decimal(prod['price'])
            prod['total_price'] = prod['price'] * prod['quantity']
            yield prod

    def __len__(self):
        """Подсчитывает количество товаров в корзине"""
        return sum(prod['quantity'] for prod in self.cart.values())

    def get_total_cart_price(self):
        """Подсчитывает стоимость всех товаров в корзине"""
        return sum(Decimal(prod['price']) * prod['quantity'] for prod in self.cart.values())

    def fix_cart(self):
        """Удаляет товар из корзины, если он был удален из БД"""
        products = self.cart.keys()
        exist_in_db = (Product.objects.filter(slug__in=products, available=True)
                       .values_list('slug', flat=True))
        products_to_remove = set(products) - set(slug for slug in exist_in_db)
        for prod in products_to_remove:
            del self.cart[prod]
        if products_to_remove:
            self.save()

    def clear_cart(self):
        """Удаляет корзину из сессии"""
        del self.session[CART_SESSION_ID]
        self.session.modified = True
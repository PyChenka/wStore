import os

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class Product(models.Model):
    """Товар в разделе Shop"""
    title = models.CharField(max_length=255)
    slug = models.SlugField(default='')
    description = models.TextField(default='')
    specification = models.JSONField(default=dict)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    available = models.BooleanField(default=True)
    time_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time_create']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'shop:single',
            kwargs={'slug': self.slug}
        )


def get_upload_path(instance, filename):
    """Создает путь для загрузки изображений в отдельную папку для каждого товара"""
    return os.path.join(instance._meta.app_label, 'images', instance.product.slug, filename, )


class Gallery(models.Model):
    """Галерея изображений товара"""
    image = models.ImageField(upload_to=get_upload_path)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'
    )


class Review(models.Model):
    """Отзыв на товар от зарегистрированного пользователя"""
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='reviews'
    )
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    name = models.CharField(max_length=64, blank=False)
    rating = models.PositiveIntegerField()
    review = models.TextField()
    date_published = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_published']

    def __str__(self):
        return f'{self.name}: {self.date_published}'


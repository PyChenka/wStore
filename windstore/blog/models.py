from django.db import models
from pytils.translit import slugify

from shop.models import Product


class Article(models.Model):
    """Статья в разделе Blog (содержит ссылки на товары)"""
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/%Y-%m-%d/')
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    products = models.ManyToManyField(
        Product,
        blank=True,
        db_table='article_products',
        related_name='articles'
    )
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-time_create']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:50]
        super().save(*args, **kwargs)

    TEMPLATE_PREVIEW = 'includes/article_preview.html'




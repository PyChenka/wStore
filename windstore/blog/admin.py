from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'show_image',
        'title',
        # 'show_products',
        'time_create',
        'time_update',
        'is_published',
    )
    list_display_links = ('title', )
    filter_horizontal = ('products', )
    search_fields = ('title', )
    list_filter = ('time_create', )
    fields = (
        'show_image',
        'title',
        'content',
        'image',
        'products',
    )
    readonly_fields = ('show_image', )

    # def show_products(self, obj):
    #     """Отображает ссылки на товары из статьи (ManyToManyField) на главной странице админки"""
    #     return [prod.images.first().image for prod in obj.products.all()]

    def show_image(self, obj):
        """Отображает изображения на главной странице админки"""
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width=50>')

    show_image.short_description = 'image'


admin.site.register(Article, ArticleAdmin)

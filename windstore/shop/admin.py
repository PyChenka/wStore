from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Gallery, Product, Review


class GalleryInLine(admin.TabularInline):
    fk_name = 'product'
    model = Gallery


# @admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'show_image',
        'title',
        'price',
        'slug',
        'available',
    )
    list_display_links = ('title', )
    search_fields = ('title', )
    list_filter = ('time_create', 'price', )
    fields = (
        'title',
        'show_image',
        'slug',
        'description',
        'specification',
        'price',
        'available',
    )
    readonly_fields = ('show_image', )
    inlines = [GalleryInLine, ]

    def show_image(self, obj):
        """Отображает главное изображение из Gallery товара"""
        return mark_safe(f'<img src="{obj.images.first().image.url}" width=50>')

    show_image.short_description = 'image'


admin.site.register(Product, ProductAdmin)


from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Gallery, Product, Review


class GalleryInLine(admin.TabularInline):
    fk_name = 'product'
    model = Gallery


# @admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
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
        'main_image',
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
        return mark_safe(f'<img src="{obj.main_image.url}" width=50>')

    show_image.short_description = 'Main image preview'


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'date_published',
        'rating',
    )
    list_display_links = ('date_published', )
    list_filter = ('date_published', 'rating', )
    readonly_fields = (
        'name',
        'customer',
        'product',
        'rating',
        'review',
        'date_published',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)


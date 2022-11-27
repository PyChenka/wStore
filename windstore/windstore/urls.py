from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import views, settings
from .views import custom_404_view, custom_error_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('shop/', include('shop.urls', namespace='shop')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]

handler404 = custom_404_view
handler500 = custom_error_view

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

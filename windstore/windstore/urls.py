from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import views, settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('shop/', include('shop.urls', namespace='shop')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

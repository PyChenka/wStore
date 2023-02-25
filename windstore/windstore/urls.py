from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import settings
from .views import *

urlpatterns = [
    path('debug/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
    path('', MainPage.as_view(), name='main'),
    path('shop/', include('shop.urls', namespace='shop')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('search/', include('search.urls', namespace='search')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('profile/', Profile.as_view(), name='profile'),
    path('orders/', include('orders.urls', namespace='orders')),
    path('subscribe/', include('mailings.urls', namespace='subscribe')),
    path('about/', about, name='about'),
]

handler404 = custom_404_view
handler500 = custom_error_view

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

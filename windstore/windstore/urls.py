from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import settings
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
    path('profile/<str:username>/', profile, name='profile'),
    path('', MainPage.as_view(), name='main'),
    path('shop/', include('shop.urls', namespace='shop')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('about/', about, name='about'),
    path('contact/', include('contact.urls', namespace='contact')),
    path('search/', include('search.urls', namespace='search')),
]

handler404 = custom_404_view
handler500 = custom_error_view

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views
from .views import ContactCreate

app_name = 'contact'

urlpatterns = [
    path('', ContactCreate.as_view(), name='contact'),
    path('done/', views.contact_done, name='done')
    ]

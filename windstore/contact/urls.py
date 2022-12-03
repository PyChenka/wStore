from django.urls import path
from .views import ContactCreate, contact_done

app_name = 'contact'

urlpatterns = [
    path('', ContactCreate.as_view(), name='contact'),
    path('done/', contact_done, name='done')
    ]

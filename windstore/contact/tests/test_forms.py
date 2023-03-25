from django.test import TestCase
from django.urls import reverse

from contact.models import Contact


class ContactFormTest(TestCase):

    def setUp(self):
        self.form_data = {
            'first_name': 'Имя',
            'email': 'test@mail.oops',
            'message': 'Hello',
        }

    def test_create_contact(self):
        """Валидная форма создает запись в Contact"""
        contact_count = Contact.objects.count()
        self.response = self.client.post(
            reverse('contact:contact'),
            data=self.form_data,
            follow=True
        )
        self.assertEqual(Contact.objects.count(), contact_count + 1)
        self.assertTrue(
            Contact.objects.filter(
                first_name='Имя',
                email='test@mail.oops',
                message='Hello'
            ).exists()
        )

    def test_redirect_after_creating(self):
        """Перенаправляет на contact:done успешно"""
        response = self.client.post(
            reverse('contact:contact'),
            data=self.form_data,
            follow=True
        )
        self.assertRedirects(response, reverse('contact:done'))

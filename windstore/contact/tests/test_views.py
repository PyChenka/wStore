from django.test import TestCase, Client
from django.urls import reverse


class ContactViewTest(TestCase):

    def test_contact_views_use_correct_templates(self):
        """По адресам страниц contact:contact, contact:done загружаются верные шаблоны"""
        pages = {
            reverse('contact:contact'): 'contact/contact.html',
            reverse('contact:done'): 'done_message.html',
        }
        for reverse_name, temp in pages.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.client.get(reverse_name)
                self.assertTemplateUsed(response, temp)

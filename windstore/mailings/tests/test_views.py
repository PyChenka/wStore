from http import HTTPStatus

from django.test import TestCase, Client
from django.urls import reverse


class SubscribeViewTest(TestCase):

    def test_subscribe_done_view_uses_correct_templates(self):
        """По адресу страницы subscribe:done загружается верный шаблон"""
        response = self.client.get(reverse('subscribe:done'))
        self.assertTemplateUsed(response, 'done_message.html')

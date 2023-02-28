from django.test import TestCase
from django.urls import reverse

from mailings.models import MailingList


class SubscribeFormTest(TestCase):

    def setUp(self):
        self.subscriber = MailingList.objects.create(
            email='mail@mail.oops'
        )

    def test_create_subscriber(self):
        """Валидная форма создает запись в MailingList"""
        subscribers_count = MailingList.objects.count()
        form_data = {
            'email': 'test@mail.oops',
        }
        response = self.client.post(
            reverse('subscribe:form'),
            data=form_data,
            follow=True
        )
        self.assertEqual(MailingList.objects.count(), subscribers_count + 1)
        self.assertTrue(
            MailingList.objects.filter(
                email='test@mail.oops',
            ).exists()
        )

    def test_existing_email_error(self):
        """Возвращается страница ошибки при вводе существующего email"""
        form_data = {
            'email': 'mail@mail.oops',
        }
        response = self.client.post(
            reverse('subscribe:form'),
            data=form_data,
            follow=True
        )
        self.assertTemplateUsed(response, 'errors/custom_error.html')
        self.assertFalse(
            MailingList.objects.filter(
                email='test@mail.oops',
            ).exists()
        )

    def test_redirect_after_creating(self):
        """Перенаправляет на subscribe:done успешно"""
        form_data = {
            'email': 'test@mail.oops',
        }
        response = self.client.post(
            reverse('subscribe:form'),
            data=form_data,
            follow=True
        )
        self.assertRedirects(response, reverse('subscribe:done'))

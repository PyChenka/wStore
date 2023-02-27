from http import HTTPStatus

from django.test import TestCase, Client


class ContactURLTest(TestCase):

    def test_contact_done_url_exists(self):
        """Страница подтверждения отправки формы /contact/done/ доступна"""
        response = self.client.get('/contact/done/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_contact_done_url_uses_correct_template(self):
        """По адресу /contact/done/ загружается верный шаблон"""
        response = self.client.get('/contact/done/')
        self.assertTemplateUsed(response, 'done_message.html')
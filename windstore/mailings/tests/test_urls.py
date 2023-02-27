from http import HTTPStatus

from django.test import TestCase, Client


class SubscribeURLTest(TestCase):

    def test_subscribe_done_url_exists(self):
        """Страница подтверждения отправки формы /subscribe/done/ доступна"""
        response = self.client.get('/subscribe/done/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_contact_done_url_uses_correct_template(self):
        """По адресу /subscribe/done/ загружается верный шаблон"""
        response = self.client.get('/subscribe/done/')
        self.assertTemplateUsed(response, 'done_message.html')
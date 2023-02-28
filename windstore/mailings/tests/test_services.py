from http import HTTPStatus

from django.test import TestCase

from mailings.services import add_to_unisender_common_list


class ServicesTest(TestCase):

    def test_add_to_unisender_func_sends_a_request(self):
        """Отправляется запрос на добавление в список рассылок Unisender"""
        data = 'testmail@mail.ts'
        result = add_to_unisender_common_list(data)
        self.assertEqual(result.status_code, HTTPStatus.OK)

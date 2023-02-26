from django.test import TestCase

from contact.models import Contact


class ContactModelTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.contact = Contact.objects.create(
            first_name='Гость'*10,
            email='111',
            message=' ',
        )

    def test_object_name_is_email_field(self):
        """Строковое представление совпадает с полем email"""
        contact = ContactModelTest.contact
        expected_object_name = contact.email
        self.assertEqual(expected_object_name, str(contact), msg='Неверное строковое представление.')

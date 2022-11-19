import unittest

from django.urls import reverse
from django.urls import resolve

from django.test import TestCase

from contact_us.models import ContactUs


class TestModel(TestCase):

    def setUp(self):
        self.customer_request = ContactUs.objects.create(
            full_name='Horizon Shop',
            email='horizon.shop@gmail.com',
            comment='Test POST Contact Us Form!'
        )

    def tearDown(self):
        print('tearDown')

    def test_new_entry_contact_us_model(self):
        request = self.customer_request

        self.assertTrue(isinstance(request, ContactUs))

    def test_return_entry_contact_us_model(self):
        request = self.customer_request

        self.assertEqual(str(request), 'Horizon Shop')

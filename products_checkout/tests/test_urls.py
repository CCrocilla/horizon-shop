import unittest

from django.urls import reverse
from django.urls import resolve

from django.test import TestCase

from products_checkout.views import CheckoutView


class TestCheckout(TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def test_url_checkout_view(self):
        url = resolve(reverse('checkout'))
        self.assertEquals(url.func.view_class, CheckoutView)

import unittest

from django.urls import reverse
from django.urls import resolve

from django.test import TestCase

from products_cart.views import CartView


class TestCart(TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def test_url_cart_view(self):
        url = resolve(reverse('cart'))
        self.assertEquals(url.func.view_class, CartView)

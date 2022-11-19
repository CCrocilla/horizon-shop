import unittest

from django.test import TestCase

from django.urls import reverse
from django.urls import resolve

from .views import WishlistView


class TestWishlist(TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def test_url_wishlist_view(self):
        url = resolve(reverse('products-wishlist'))
        self.assertEquals(url.func.view_class, WishlistView)

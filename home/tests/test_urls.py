import unittest

from django.urls import reverse
from django.urls import resolve

from django.test import TestCase
from django.test import Client

from home.views import HomeView


class TestUrls(TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def test_url_homepage_view(self):
        url = resolve(reverse('homepage'))
        self.assertEquals(url.func.view_class, HomeView)

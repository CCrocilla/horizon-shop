import unittest

from django.urls import reverse
from django.urls import resolve

from django.test import TestCase
from django.test import Client

from home.views import HomeView


class TestViews(TestCase):

    def setUp(self):
        print('setUp')
        self.client = Client()
        self.homepage_url = reverse('homepage')

    def tearDown(self):
        print('tearDown')

    def test_GET_view_homepage(self):
        # GET Request
        response = self.client.get(self.homepage_url)
        # Check if response is 200.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

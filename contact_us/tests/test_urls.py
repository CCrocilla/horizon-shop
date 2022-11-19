import unittest

from django.urls import reverse
from django.urls import resolve

from django.test import TestCase

from contact_us.views import ContactUsView
from contact_us.views import TermsView


class TestUrls(TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def test_url_contact_us_view(self):
        url = resolve(reverse('contact_us'))
        self.assertEquals(url.func.view_class, ContactUsView)

    def test_url_terms_and_condition_view(self):
        url = resolve(reverse('terms'))
        self.assertEquals(url.func.view_class, TermsView)

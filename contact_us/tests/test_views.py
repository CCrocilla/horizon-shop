import unittest

from django.urls import reverse
from django.urls import resolve

from django.test import TestCase
from django.test import Client

from contact_us.views import ContactUsView
from contact_us.views import TermsView

from contact_us.models import ContactUs


class TestViews(TestCase):

    def setUp(self):
        print('setUp')
        self.client = Client()
        self.contact_us_url = reverse('contact_us')
        self.terms_url = reverse('terms')

    def tearDown(self):
        print('tearDown')

    def test_GET_view_contact_us(self):
        # GET Request
        response = self.client.get(self.contact_us_url)
        # Check if response is 200.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact_us/contact-us.html')

    def test_GET_view_terms_and_condition(self):
        # GET Request
        response = self.client.get(self.terms_url)
        # Check if response is 200.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact_us/terms.html')

    def test_POST_form_contact_us(self):
        # POST Request
        response = self.client.post(self.contact_us_url, {
            'full_name': 'Horizon Shop',
            'email': 'horizon.shop@gmail.com',
            'comment': 'Test POST Contact Us Form!',
        })
        # Check if response is 302 Code as the redirect status
        # response code indicates that the resource requested
        # has been temporarily moved to the URL given by the Location header.
        self.assertEqual(response.status_code, 302)

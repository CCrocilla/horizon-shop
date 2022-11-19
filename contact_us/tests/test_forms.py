from django.test import TestCase
from contact_us.forms import ContactUsForm


class TestForms(TestCase):

    def setUp(self):
        self.contact_form = ContactUsForm(
            data={
                'fullname': 'Horizon Shop',
                'email': 'horizon.shop@gmail.com',
                'message': 'Test Contact Us Form!',
            })

    def tearDown(self):
        print('tearDown')

    def test_contact_form_is_valid(self):
        """
        If the form is incomplete the form cannot
        be submitted as it is not valid.
        """
        contact_form = self.contact_form
        self.assertFalse(contact_form.is_valid())

    def test_contact_form_no_data(self):
        """
        If the form is empty the form cannot be
        submitted as it is not valid.
        """
        contact_form = ContactUsForm(data={})
        self.assertFalse(contact_form.is_valid())

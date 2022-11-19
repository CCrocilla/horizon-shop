import unittest

from django.urls import reverse
from django.urls import resolve

from django.contrib.auth.models import User

from django.test import TestCase

from products.models import Product
from products.models import Category
from products.models import SubCategory


class TestModels(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name='Console & Videogames',
            slug='console-and-videogames'
            )
        self.subcategory = SubCategory.objects.create(
            name='Console',
            slug='console'
            )
        self.created_by = User.objects.create(
            username='Admin'
            )
        self.product = Product.objects.create(
            created_by_id=self.created_by.id,
            category_id=self.category.id,
            subcategory_id=self.subcategory.id,
            title='PS5',
            slug='ps5',
            price='500.00',
            product_status=0,
            )

    def tearDown(self):
        print('tearDown')

    def test_return_data_category_model(self):
        """
        Check if data return from Category Model
        is the Category's Name.
        """
        data = self.category
        self.assertEqual(str(data), 'Console & Videogames')       

    def test_return_data_product_model(self):
        """
        Check if data return from Sub-Category Model
        is the Sub-Category's Name.
        """
        data = self.subcategory
        self.assertEqual(str(data), 'Console')

    def test_return_data_product_model(self):
        """
        Check if data return from Product
        Model is the Product's Title.
        """
        data = self.product
        self.assertEquals(str(data), 'PS5')

    def test_return_incorrect_data_product_model(self):
        """
        Check if data returned is not equal to searched 
        data in Products Model.
        """
        data = self.product
        self.assertNotEquals(str(data), 'PS6')

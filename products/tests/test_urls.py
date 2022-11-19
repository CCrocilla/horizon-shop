import unittest

from django.urls import reverse
from django.urls import resolve

from django.contrib.auth.models import User

from django.test import TestCase
from django.test import Client

from products.models import Product
from products.models import Category
from products.models import SubCategory

from products.views import ProductDetailsView
from products.views import AllProductsListView


class TestUrls(TestCase):

    def setUp(self):
        self.client = Client()
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

    def test_url_all_products_view(self):
        url = resolve(reverse('all_products'))
        self.assertEquals(url.func.view_class, AllProductsListView)

    def test_url_product_details_view(self):
        url = resolve(reverse('product_details', args=['slug']))
        self.assertEquals(url.func.view_class, ProductDetailsView)

    def test_get_absolute_url_category(self):
        url = self.client.get(
            reverse('search_by', args=['console-and-videogames']))
        self.assertEquals(url.status_code, 200)


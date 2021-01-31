from django.test import TestCase
from django.shortcuts import resolve_url
from product_manager.core.models import Product

# Create your tests here.
class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get(resolve_url('list'))

    def test_get(self):
        self.assertEqual(self.response.status_code, 200)


class ProductModelTest(TestCase):
    def setUp(self):
        self.obj = Product(
            name='Arroz',
            value=15,
            description='Random description here'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Product.objects.exists())

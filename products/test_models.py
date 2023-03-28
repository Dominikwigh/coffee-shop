from django.test import TestCase
from .models import Category, Product


class TestProductModels(TestCase):
    fixtures = ['categories.json', 'products.json']

    def test_product_name(self):
        product = Product.objects.get(pk=1)
        self.assertEqual(product.name, 'Lavazza Oro')
        self.assertNotEqual(product.name, 'Test name')
        self.assertEqual(str(product), product.name)

    def test_product_description(self):
        product = Product.objects.get(pk=1)
        self.assertEqual(
            product.description, (
                "The Lavazza coffee beans are a blend of Arabica from Brazil, RainForest certified. Enjoy a strong coffee with gourmet notes of cereals and dried fruit. 1kg."))
        self.assertNotEqual(product.description, 'test description')

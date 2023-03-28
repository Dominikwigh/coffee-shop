from django.test import TestCase

from products.models import Product
from .models import Order


class testOrderModels(TestCase):

    def setup(self):
        Order.objects.create(
            full_name='testname',
            email='test@test.com',
            phone_number='01234567890',
            street_address1='test',
            town_or_city='test',
            country='GB'
        )

    def test_order_string_method(self):
        order_number = Order.objects.create(order_number='100')
        self.assertEqual(str(order_number), '100')

    def test_update_total(self):
        order_total = 100
        grand_total = order_total
        self.assertEqual(grand_total, 100)



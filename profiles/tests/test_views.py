from django.test import TestCase
from django.contrib.auth.models import User
from checkout.models import Order


class TestProfileView(TestCase):
    """ Test Cases """

    def test_show_profile(self):
        """
        Test case to register, login and 
        show profile
        """
        user = User.objects.create_user(
            'testuser', 'testuser@test.com', 'testuserpassword'
        )
        self.client.force_login(user, backend=None)
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('profiles/profile.html')

    def test_order_history(self):
        """
        Testing order details view
        by creating test order and accesing URL.
        """
        order = Order.objects.create(
            full_name='testuser',
            email='testuser@test.com',
            phone_number='123456',
            postcode='123456',
            town_or_city='testtown',
            street_address1='Address1',
            street_address2='Address2',
            county='testcounty',
            grand_total=17.59,
            delivery_cost=1.60,
            order_total=15.99
        )
        response = self.client.get(
            f'/profile/order_history/{order.order_number}/'
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('checkout/checkout_success.html')
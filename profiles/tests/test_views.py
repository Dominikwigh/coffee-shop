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
            'unittestuser', 'unittestuser@test.com', 'unittestuserpassword'
        )
        self.client.force_login(user, backend=None)
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('profiles/profile.html')

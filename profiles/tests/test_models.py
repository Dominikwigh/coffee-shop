from django.test import TestCase
from profiles.models import UserProfile
from django.contrib.auth.models import User
import string
from django.shortcuts import get_object_or_404


class TestUserProfile(TestCase):
    """ Test the models for profile app """
    def setUp(Self):
        user = User.objects.create_user(
        'unittestuser', 'unittestuser@test.com', 'unittestuserpassword'),

    def test_profile_str(self):
        """Test UserProfile string method"""
        user = get_object_or_404(User, username="unittestuser")
        user_profile = get_object_or_404(UserProfile, user=user)
        self.assertEqual(str(user_profile), "unittestuser")

    def test_create_user_profile_receiver(self):
        """Test UserProfile create receiver"""
        # Create new standard user
        newuser = User.objects.create_user(
            'unittestuser2', 'unittestuser2@test.com', 'unittestuser2password')
        user_profile = get_object_or_404(UserProfile, user=newuser)
        # Update user
        self.assertTrue(user_profile)

    def test_update_user_profile_receiver(self):
        """Test UserProfile update receiver"""
        # Get standard user
        user = get_object_or_404(User, username="unittestuser")
        # Update username
        user.username = "unittestuserupdated"
        user.save()
        user_profile = get_object_or_404(UserProfile, user=user)
        # Test updated user
        self.assertTrue(user_profile)
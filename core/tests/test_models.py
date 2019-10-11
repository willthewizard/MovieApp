from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from core import models

def sample_user(email='test@fintelics.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)

class ModelTests(TestCase):

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = "will@fintelics.com"
        user = get_user_model().objects.create_user(email, 'password123')

        self.assertEqual(user.email, email.lower())
    
    def test_create_new_superuser(self):
        """Test for creating the new super user"""
        user = get_user_model().objects.create_superuser(
            "super@fintelics.com",
            "super123"
        )
        self.assertEqual(user.is_superuser,True)
        self.assertEqual(user.is_staff,True)

    def test_movie_str(self):
        """Test the tag string representation"""
        movie = models.Movie.objects.create(
            movie_id = 'mv1',
            name='Kill Bill'
        )

        self.assertEqual(str(movie), movie.name)
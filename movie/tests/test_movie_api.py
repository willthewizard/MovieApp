from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Movie

# from movie.serializers import TagSerializer

MOVIE_URL = reverse('movie:movie-list')

class PublicMovieApiTests(TestCase):
    """Test public available movie API """
    
    def setUp(self):
        self.client = APIClient()
    
    def test_login_required(self):
        """Test login required for """
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

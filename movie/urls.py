from django.urls import path, include
from rest_framework.routers import DefaultRouter

from movie import views


router = DefaultRouter()
router.register('room', views.RoomViewSet)
router.register('movie', views.MovieViewSet)
router.register('tickets', views.TicketsViewSet)
router.register('order', views.OrderViewSet)

app_name = 'movie'

urlpatterns = [
    path('', include(router.urls))
]

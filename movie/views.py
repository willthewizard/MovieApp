from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser

from core.models import Movie, Room, Tickets,Order
from django.core.exceptions import ValidationError


from movie import serializers


class BaseTicketAttrViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin):
    """Base viewset for user owned recipe attributes"""
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter().distinct()



class RoomViewSet(BaseTicketAttrViewSet):
    """Manage room in the database"""
    queryset = Room.objects.all()
    serializer_class = serializers.RoomSerializer

    def perform_create(self, serializer):
        """Create a new room"""
        serializer.save()

class MovieViewSet(BaseTicketAttrViewSet):
    """Manage movie in the database"""
    queryset = Movie.objects.all()
    serializer_class = serializers.MovieSerializer

    def perform_create(self, serializer):
        print(self.request.data.get("room_id"))
        duplicated_showtimes = self.queryset.filter(
            room_id=self.request.data.get("room_id"),
            showtime=self.request.data.get("showtime")
        )

        serializer.save()
class TicketsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TicketsSerializer
    queryset = Tickets.objects.all()
    def _params_to_ints(self, qs):
        """Convert a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        """Retrieve the tickets object"""
        queryset = self.queryset
        movie_id = self.request.query_params.get('movie_id')
        room_id = self.request.query_params.get('room_id')
        if movie_id:
            movie_id_int = self._params_to_ints(movie_id)
            queryset = queryset.filter(movie_id=movie_id_int)
        if room_id:
            room_id_int = self._params_to_ints(room_id)
            queryset = queryset.filter(room_id=room_id_int)

        return queryset

    def perform_create(self,serializer):
        serializer.save()
class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TicketsPurchaseSerializer
    queryset = Order.objects.all()
    def perform_create(self, serializer):
        serializer.create_purchase_order(self.request.data.get('tickets_id'))
        serializer.save()

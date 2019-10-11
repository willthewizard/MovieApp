from rest_framework import serializers

from core.models import Movie, Room, Tickets, Order


class RoomSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""

    class Meta:
        model = Room
        fields = ('id', 'total_seat')
        read_only_fields = ('id',)

class MovieSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""

    class Meta:
        model = Movie
        fields = ('id', 'room_id','name','showtime')
        read_only_fields = ('id',)

class TicketsSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""
    # room_id = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     queryset=Room.objects.all()
    # )
    # movie_id = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     queryset=Movie.objects.all()
    # )
    class Meta:
        model = Tickets
        fields = ('id', 'movie_id','room_id','ticket_available','price')
        read_only_fields = ('id',)

class TicketsPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order 
        fields = ('id','tickets_id')
        read_only_fields = ('id',)
    def create_purchase_order(self,tickets_id):
        ticket_count = Tickets.objects.filter(id=tickets_id).values('ticket_available')[0]['ticket_available']
        print(ticket_count)
        new_ticket_count = ticket_count -1
        if new_ticket_count <0:
            raise ValueError('No more tickets available 0')
        Tickets.objects.filter(id=tickets_id).update(ticket_available=new_ticket_count)
        return
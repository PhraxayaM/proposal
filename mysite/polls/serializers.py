from rest_framework import serializers

from .models import Event, Event_Item


class EventItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event_Item
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    items = EventItemSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Event
        fields = "__all__"

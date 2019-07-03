# from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Event, Event_Item
from .serializers import EventSerializer

class EventList(APIView):
    def get(self, request):
        events = Event.objects.all()[:20]
        data = EventSerializer(events, many=True).data
        return Response(data)

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

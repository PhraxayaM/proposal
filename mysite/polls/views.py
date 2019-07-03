

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render

from .models import Event, Event_Item
from .serializers import EventSerializer

class EventList(APIView):
    def get(self, request):
        events = Event.objects.all()[:20]
        data = EventSerializer(events, many=True).data
        return render(request, 'events/index.html', {'latest_event_list': data})


class EventDetail(APIView):
    def get(self, request, event_id):
        event = Event.objects.get(id=event_id)
        data = EventSerializer(event, many=False).data
        return render(request, 'events/detail.html', {'event': data})

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

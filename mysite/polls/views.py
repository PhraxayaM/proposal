
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Event, Event_Item
from .serializers import EventSerializer

def index(request):
    event_list = Event.objects.order_by('-event_date')[:5]
    context = {
        'event_list': event_list,
    }
    return render(request, 'events/index.html', context)

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event_item = Event_Item.objects.filter(event=event)
    context = {
        'event': event,
        'event_item': event_item
    }
    return render(request, 'events/detail.html', context)



class EventList(APIView):
    def get(self, request):
        events = Event.objects.all()[:20]
        data = EventSerializer(events, many=True).data
        return render(request, 'events/index.html', {'latest_event_list': data})


class EventDetail(viewsets.ViewSet):
    def list(self, request, event_id):
        event = Event.objects.get(id=event_id)
        data = EventSerializer(event).data
        return render(request, 'events/detail.html', {'event': data})

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

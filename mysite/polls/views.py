
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from .models import Event, Event_Item
from .serializers import EventSerializer
from . import forms

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

def new_event(request):
    if request.method == 'POST':
        form = forms.EventForm(request.POST)
        if form.is_valid():
            event = Event(event_name=form.cleaned_data["event_name"], event_date=form.cleaned_data["event_date"])
            event.save()
            return redirect('polls:index')
    elif request.method == 'GET':
        form = forms.EventForm()
        return render(request, 'events/new_event.html', {'form': form})





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

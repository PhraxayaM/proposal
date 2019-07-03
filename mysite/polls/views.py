from django.http import Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Event




def index(request):
    latest_event_list = Event.objects.order_by('-event_date')[:5]
    context = {'latest_question_list': latest_event_list}
    return render(request, 'polls/index.html', context)

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'polls/detail.html', {'event': event})

def results(request, event_id):
    response = "You're looking at the results of event %s."
    return HttpResponse(response % event_id)

def time(request, event_id):
    return HttpResponse("Event starts at %s." % event_id)

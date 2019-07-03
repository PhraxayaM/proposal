from django.urls import path

from . import views
from .views import EventList

urlpatterns = [
    # path('', views.index, name='index'),
    path("events/", EventList.as_view(), name="event_list"),
]

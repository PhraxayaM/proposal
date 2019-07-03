from django.urls import path

from . import views
from .views import EventList, EventDetail


app_name = 'polls'
urlpatterns = [
    # path('', views.index, name='index'),
    path("events/", EventList.as_view(), name="event_list"),
    path('<int:event_id>/', EventDetail.as_view(), name='detail'),
]

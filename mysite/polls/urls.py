from django.urls import path

from . import views
from .views import EventList, EventDetail


app_name = 'polls'
urlpatterns = [
    path('events/', views.index, name='index'),
    path('<int:event_id>/', views.detail, name='detail'),
    path('events/create', views.new_event, name='create'),

    # path("events/", views.IndexView.as_view(), name="event_list"),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]

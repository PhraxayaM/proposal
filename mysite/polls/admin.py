
from django.contrib import admin
from .models import Event_Item, Event
# Register your models here.

class EventInline(admin.StackedInline):
    model = Event_Item
    extra = 3

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['event_name']}),
        ('Date information', {'fields': ['event_date']}),
    ]
    inlines = [EventInline]


admin.site.register(Event, EventAdmin)

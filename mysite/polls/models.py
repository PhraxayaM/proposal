# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_date = models.DateField('event date')


class Event_Item(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    item_text = models.CharField(max_length=200)
    item_time = models.TimeField('Start time')

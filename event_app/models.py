# models.py

from django.db import models
from django.urls import reverse

class Event(models.Model):
    event_id = models.AutoField(primary_key=True, default='')
    event_init_date = models.DateField()
    event_last_date = models.DateField()
    event_title = models.CharField(max_length=200)
    event_place = models.CharField(max_length=200)
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('event_app:event_detail', args=[str(self.id)])

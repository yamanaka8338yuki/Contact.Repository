# urls.py

from django.urls import path
from . import views

app_name = 'event_app'

urlpatterns = [
    path('calendar/', views.event_calendar, name='event_calendar'),
    path('add/', views.add_event, name='add_event'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event/<int:event_id>/edit/', views.edit_event, name='edit_event'),
    path('event/<int:event_id>/delete/', views.delete_event, name='delete_event'),
    path('api/events/', views.api_events, name='api_events'),
]

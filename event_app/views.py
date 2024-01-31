# views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Event
from .forms import EventForm
from django.http import JsonResponse

def event_calendar(request):
    events = Event.objects.all()
    return render(request, 'event_app/event_calendar.html', {'events': events})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event has been successfully added.')
            return redirect('event_app:event_calendar')
    else:
        form = EventForm()
    return render(request, 'event_app/add_event.html', {'form': form})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'event_app/event_detail.html', {'event': event})

def api_events(request):
    events = Event.objects.all()
    event_list = []
    for event in events:
        event_list.append({
            'title': event.event_title,
            'start': event.event_init_date.isoformat(),
            'end': event.event_last_date.isoformat(),
            'url': event.get_absolute_url(),
            'place': event.event_place,
            'comments': event.comments,
        })

    return JsonResponse(event_list, safe=False)
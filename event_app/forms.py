# forms.py

from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_init_date', 'event_last_date', 'event_title', 'event_place', 'comments']
        widgets = {
            'event_init_date': forms.DateInput(attrs={'type': 'date'}),
            'event_last_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'event_title': 'タイトル',
            'event_init_date': '開始日',
            'event_last_date': '終了日',
            'event_place': '場所',
            'comments': 'コメント',
        }

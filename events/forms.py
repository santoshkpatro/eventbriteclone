from django import forms
from .models import Event


class AddEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'description', 'event_time', 'event_date', 'location', 'thumbnail')

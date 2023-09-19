from django import forms
from .models import Booking


class AvailabilityForm(forms.Form):
    rooms = (
        ('Oiá', 'Oiá'),
        ('Ogum', 'Ogum'),
    )

    room_choices = forms.ChoiceField(choices=rooms, required=True)
    check_in = forms.DateField(input_formats=["%Y-%m-%d", ], required=True)
    check_out = forms.DateField(input_formats=["%Y-%m-%d", ], required=True)

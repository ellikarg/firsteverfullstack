from django import forms
from django.forms import ModelForm
from .models import Booking



class AvailabilityForm(ModelForm):
    class Meta:
        model = Booking
        fields = ('user', 'room', 'check_in', 'check_out')


    # check_in = forms.DateField(input_formats=["%b %d, %Y", ], required=True)
    # check_out = forms.DateField(input_formats=["%b %d, %Y", ], required=True)

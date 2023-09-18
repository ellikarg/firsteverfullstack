from django import forms


class AvailabilityForm(forms.Form):

    check_in = forms.DateField(input_formats=["%b %d, %Y", ], required=True)
    check_out = forms.DateField(input_formats=["%b %d, %Y", ], required=True)

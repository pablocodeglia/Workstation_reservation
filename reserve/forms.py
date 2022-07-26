# from attr import fields
from django import forms
from django.forms import ModelForm
from .models import Reservations
import datetime 
from django.core.exceptions import ValidationError

class DateInput(forms.DateInput):
    input_type = 'date'

class ReservationDateForm(forms.Form):
    date = forms.DateField(widget = DateInput)
    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError('No time travelling! Today onwards dates only :)')
        return date


class MakeReservationForm(ModelForm):
    class Meta:
        model = Reservations
        fields = ['workstation_id', 'employee', 'reservation_date']
        
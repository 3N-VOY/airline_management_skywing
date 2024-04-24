from secrets import choice
from django import forms
from base import models


class SaveFlights(forms.ModelForm):
    flight_number = forms.CharField(max_length=250)
    origin = forms.ModelChoiceField(queryset=models.City.objects.all())
    destination = forms.ModelChoiceField(queryset=models.City.objects.all())
    airplane= forms.ModelChoiceField(queryset=models.Airplane.objects.all())
    departure_time = forms.DateTimeField()
    arrival_time = forms.DateTimeField()
    date = forms.DateTimeField()
    staff = forms.ModelMultipleChoiceField(queryset=models.Staff.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = models.Flight
        fields = ('flight_number', 'origin', 'destination', 'airplane', 'departure_time', 'arrival_time', 'date', 'staff',)

    # def clean_flight_number(self):
    #     flight_number = self.cleaned_data.get('flight_number')
    #     flight_id = self.instance.id if self.instance else 0

    #     try:
    #         if flight_id > 0:
    #             flight = models.Flight.objects.exclude(id=flight_id).get(flight_number=flight_number)
    #         else:
    #             flight = models.Flight.objects.get(flight_number=flight_number)
    #     except models.Flight.DoesNotExist:
    #         return flight_number
    #     raise forms.ValidationError("Flight number already exists")
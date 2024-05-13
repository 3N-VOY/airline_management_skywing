from django.forms import ModelMultipleChoiceField, SelectMultiple
from django import forms
from base import models
from staff.models import Staff
from users.models import Passenger

class SaveFlights(forms.ModelForm):
    flight_number = forms.CharField(max_length=250)
    origin = forms.ModelChoiceField(queryset=models.City.objects.all())
    destination = forms.ModelChoiceField(queryset=models.City.objects.all())
    airplane = forms.ModelChoiceField(queryset=models.Airplane.objects.all())
    departure_time = forms.DateTimeField()
    arrival_time = forms.DateTimeField()
    date = forms.DateTimeField()
    captain = forms.ModelChoiceField(queryset=models.Staff.objects.filter(role='Pilot'))
    copilot = forms.ModelChoiceField(queryset=models.Staff.objects.filter(role='Pilot'))
    flight_attendants = forms.ModelMultipleChoiceField(queryset=Staff.objects.filter(role='FlightAttendant'), widget=SelectMultiple(attrs={'multiple': True, 'id': 'flight_attendants_dropdown'}))
    maintenance_crew = forms.ModelMultipleChoiceField(queryset=models.Staff.objects.filter(role='Maintenance Crew'))

    class Meta:
        model = models.Flight
        fields = ('flight_number', 'origin', 'destination', 'airplane', 'departure_time', 'arrival_time', 'date', 'captain', 'copilot', 'flight_attendants', 'maintenance_crew')




class ReservationForm(forms.ModelForm):
    class Meta:
        model = models.Reservation
        fields = ('flight', 'passenger', 'seat_number', 'class_type')

class PassengerForm(forms.ModelForm):
    class Meta:
        model = models.Passenger
        fields = ('email', 'first_name', 'last_name', 'phone', 'address')

class StaffForm(forms.ModelForm):
    class Meta:
        model = models.Staff
        fields = ('employee_number', 'first_name', 'last_name', 'salary', 'password', 'phone', 'email', 'department', 'role')





# from secrets import choice
# from django import forms
# from base import models


# class SaveFlights(forms.ModelForm):
#     flight_number = forms.CharField(max_length=250)
#     origin = forms.ModelChoiceField(queryset=models.City.objects.all())
#     destination = forms.ModelChoiceField(queryset=models.City.objects.all())
#     airplane= forms.ModelChoiceField(queryset=models.Airplane.objects.all())
#     departure_time = forms.DateTimeField()
#     arrival_time = forms.DateTimeField()
#     date = forms.DateTimeField()
#     staff = forms.ModelMultipleChoiceField(queryset=models.Staff.objects.all(), widget=forms.CheckboxSelectMultiple)

#     class Meta:
#         model = models.Flight
#         fields = ('flight_number', 'origin', 'destination', 'airplane', 'departure_time', 'arrival_time', 'date', 'staff',)

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
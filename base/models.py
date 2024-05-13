from django.db import models
from users.models import Passenger
from staff.models import Pilot, Staff


class Airplane(models.Model):
    serial_number = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.manufacturer} {self.model}"
    
class City(models.Model):
    city_name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    
    def __str__(self):
        return self.city_name

class Flight(models.Model):
    flight_number = models.CharField(max_length=20)
    origin = models.ForeignKey(City, related_name='departing_flights', on_delete=models.CASCADE)
    destination = models.ForeignKey(City, related_name='arriving_flights', on_delete=models.CASCADE)
    date = models.DateField()
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    pilots = models.ManyToManyField(Pilot, related_name='piloted_flights')
    staff = models.ManyToManyField(Staff, related_name='flights')


    def __str__(self):
        return f"Flight {self.flight_number} from {self.origin} to {self.destination}"




class FlightStop(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    sequence = models.IntegerField()

    class Meta:
        unique_together = ('flight', 'sequence')

    def __str__(self):
        return f"{self.flight} Stop {self.sequence}: {self.city}"

class Reservation(models.Model):
    CLASS_CHOICES = [
        ('Economy', 'Economy'),
        ('Business', 'Business'),
        ('First', 'First'),
    ]
    
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    class_type = models.CharField(max_length=20, choices=CLASS_CHOICES)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.passenger} - {self.flight} - {self.class_type}"
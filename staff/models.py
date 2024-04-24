from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
from accounts.models import User

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Staff(User):
    employee_number = models.CharField(max_length=20)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    staff_groups = models.ManyToManyField(Group, related_name='staff_groups', blank=True)
    staff_user_permissions = models.ManyToManyField(Permission, related_name='staff_user_permissions', blank=True)
    # Add a field for role
    ROLE_CHOICES = [
        ('Pilot', 'Pilot'),
        ('FlightAttendant', 'Flight Attendant'),
        ('Security Personnel', 'Security Personnel'),
        ('Air Traffic Controllers', 'Air Traffic Controllers'),
        ('Maintenance Crew', 'Maintenance Crew'),
        ('Customer Service Representatives', 'Customer Service Representatives'),
        
    ]
    role = models.CharField(max_length=55, choices=ROLE_CHOICES, default='Other')

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

class Pilot(models.Model):
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE, primary_key=True)
    type_ratings = models.CharField(max_length=100)

    def __str__(self):
        return f"Pilot: {self.staff.last_name}, {self.staff.first_name}"


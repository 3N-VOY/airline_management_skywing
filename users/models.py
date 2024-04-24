from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
from accounts.models import User



class Passenger(User):
    address = models.TextField()
    phone = models.CharField(max_length=20)
    passenger_groups = models.ManyToManyField('auth.Group', related_name='passenger_groups', blank=True)
    passenger_permissions = models.ManyToManyField('auth.Permission', related_name='passenger_user_permissions', blank=True)
   
    def __str__(self):
        return self.email
    



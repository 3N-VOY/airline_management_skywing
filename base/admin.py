from django.contrib import admin

from base.models import Airplane
from base.models import Flight
from base.models import City
from base.models import FlightStop

from users.models import Passenger
from base.models import Reservation

from staff.models import Department
from staff.models import Staff
from staff.models import Pilot

# Register your models here.
admin.site.register(Airplane)
admin.site.register(Flight)

admin.site.register(City)

admin.site.register(FlightStop)

admin.site.register(Passenger)
admin.site.register(Reservation)

admin.site.register(Department)
admin.site.register(Staff)

admin.site.register(Pilot)
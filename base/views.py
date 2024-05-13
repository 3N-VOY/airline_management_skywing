from django.shortcuts import render, get_object_or_404, redirect
from .models import Flight, Reservation
from django.http import JsonResponse
from .forms import SaveFlights, ReservationForm, PassengerForm, StaffForm
from staff.models import Pilot
from staff.models import Staff
from users.models import Passenger
from .models import Reservation
import datetime
from django.utils import timezone

def dashboard(request):
    reservations_count = Reservation.objects.count()
    flights_count = Flight.objects.count()
    passengers_count = Passenger.objects.count()
    
    now = timezone.now()
    flights_count_future = Flight.objects.filter(
        departure_time__gte=now
    ).count()

    context = {
        'reservations_count': reservations_count,
        'flights_count': flights_count,
        'flights_count_future': flights_count_future,
        'passengers_count': passengers_count
    }

    return render(request, 'base/base.html', context)

#retrieve flights
def flight_list(request):
    flights = Flight.objects.all()
    context = {'flights': flights}
    return render(request, 'base/flight_management.html', context)

#retrieve flight data for edit in modal
def flight_data(request, pk):
    flight_detail = get_object_or_404(Flight, pk=pk)
    flight_attendants = flight_detail.staff.filter(role='FlightAttendant')
    maintenance_crew = flight_detail.staff.filter(role='Maintenance Crew')
    pilots = flight_detail.pilots.all()

    if pilots:
        captain = pilots[0]
        copilot = pilots[1] if len(pilots) > 1 else None
        context = {'flight_detail': flight_detail, 
                   'flight_attendants': flight_attendants,
                   'maintenance_crew': maintenance_crew,
                   'captain': captain,
                   'copilot': copilot,
                   }
    else:
        context = {'flight_detail': flight_detail, 
                   'flight_attendants': flight_attendants,
                   'maintenance_crew': maintenance_crew,
                   'captain': None,
                   'copilot': None,
                   }
  
    return render(request, 'base/flight_data.html', context)

#flight form
def flight_form(request, pk):
    flight_detail = get_object_or_404(Flight, pk=pk)

    if request.method == 'GET':
        form = SaveFlights(instance=flight_detail)
        context = {'form': form, 'pk': pk}
        return render(request, 'base/flight_form.html', context)
        
    elif request.method == 'POST':
        form = SaveFlights(request.POST, instance=flight_detail)
        if form.is_valid():
            form.save()
            if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            else:
                print("Successfully updated flight details")
                return redirect('manage_flight')  # Assuming you have a URL named 'dashboard'
        else:
            if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
                errors = form.errors.as_json()
                return JsonResponse({'success': False, 'errors': errors}, status=400)
            else:
                print(form.errors)
                # Handle form errors
                context = {'form': form, 'pk': pk}
                return render(request, 'base/flight_form.html', context)
            
def delete_flight(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    flight.delete()
    return JsonResponse({"success": True})

  
def add_flight2(request):
    if request.method == 'GET':
        form = SaveFlights()
        context = {'form': form}
        return render(request, 'base/add_flight_form.html', context)
    
    elif request.method == 'POST':
        form = SaveFlights(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('manage_flight') 
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = SaveFlights()
    return render(request, 'base/add_flight_form.html', {'form': form})

#RESERVATION MANAGEMENT

def reservation_list(request):
    reservations = Reservation.objects.all()
    context = {'reservations': reservations}
    return render(request, 'base/reservation_management.html', context)

def reservation_data(request, pk):
    reservation_detail = get_object_or_404(Reservation, pk=pk)
    context = {'reservation_detail': reservation_detail}
    return render(request, 'base/reservation_data.html', context)

def reservation_form(request, pk):
    reservation_detail = get_object_or_404(Reservation, pk=pk)
    if request.method == 'GET':
        form = ReservationForm(instance=reservation_detail)
        context = {'form': form, 'pk': pk}
        return render(request, 'base/reservation_form.html', context)
    elif request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation_detail)
        if form.is_valid():
            form.save()
            if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            else:
                print("Successfully updated reservation details")
                return redirect('manage_reservations')  # Assuming you have a URL named 'dashboard'
        else:
            if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
                errors = form.errors.as_json()
                return JsonResponse({'success': False, 'errors': errors}, status=400)
            else:
                print(form.errors)
                # Handle form errors
                context = {'form': form, 'pk': pk}
                return render(request, 'base/reservation_form.html', context)
            

def delete_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    reservation.delete()
    return JsonResponse({"success": True})

def add_reservation(request):
    if request.method == 'GET':
        form = ReservationForm()
        context = {'form': form}
        return render(request, 'base/add_reservation_form.html', context)
    elif request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_reservations')
        else:
            return JsonResponse({'success': False, 'errors': form.errors})

#passenger management
def passenger_list(request):
    passengers = Passenger.objects.all()
    context = {'passengers': passengers}
    return render(request, 'base/passenger_management.html', context)

def passenger_data(request, pk):
    passenger_detail = get_object_or_404(Passenger, pk=pk)
    context = {'passenger_detail': passenger_detail}
    return render(request, 'base/passenger_data.html', context)

def passenger_form(request, pk):
    passenger_detail = get_object_or_404(Passenger, pk=pk)
    if request.method == 'GET':
        form = PassengerForm(instance=passenger_detail)
        context = {'form': form, 'pk': pk}
        return render(request, 'base/passenger_form.html', context)
    elif request.method == 'POST':
        form = PassengerForm(request.POST, instance=passenger_detail)
        if form.is_valid():
            form.save()
            return redirect('manage_passengers')
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    
def delete_passenger(request, pk):
    passenger = get_object_or_404(Passenger, pk=pk)
    passenger.delete()
    return JsonResponse({"success": True})

#Staff Management
def staff_list(request):
    staffs = Staff.objects.all()
    context = {'staffs': staffs}
    return render(request, 'base/staff_management.html', context)

def staff_data(request, pk):
    staff_detail = get_object_or_404(Staff, pk=pk)
    context = {'staff_detail': staff_detail}
    return render(request, 'base/staff_data.html', context)

def staff_form(request, pk):
    staff_detail = get_object_or_404(Staff, pk=pk)
    if request.method == 'GET':
        form = StaffForm(instance=staff_detail)
        context = {'form': form, 'pk': pk}
        return render(request, 'base/staff_form.html', context)
    elif request.method == 'POST':
        form = StaffForm(request.POST, instance=staff_detail)
        if form.is_valid():
            form.save()
            return redirect('manage_staff')
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
        
def staff_delete(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    staff.delete()
    return JsonResponse({"success": True})

def add_staff(request):
    if request.method == 'GET':
        form = StaffForm()
        context = {'form': form}
        return render(request, 'base/add_staff_form.html', context)
    elif request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_staff')
        else:
            return JsonResponse({'success': False, 'errors': form.errors})

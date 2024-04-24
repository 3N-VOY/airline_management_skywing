from django.shortcuts import render, get_object_or_404, redirect
from .models import Flight
from django.http import JsonResponse
from .forms import SaveFlights

def dashboard(request):
    return render(request, 'base/base.html')


#retrieve flights
def flight_list(request):
    flights = Flight.objects.all()
    context = {'flights': flights}
    return render(request, 'base/flight_management.html', context)

#retrieve flight data for edit in modal
def flight_data(request, pk):
    flight_detail = get_object_or_404(Flight, pk=pk)
    context = {'flight_detail': flight_detail}
    return render(request, 'base/flight_form.html', context)

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
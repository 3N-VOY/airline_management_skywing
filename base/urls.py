from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('manage-flights/', views.flight_list, name='manage_flight'),
    path('flight-data/<int:pk>/', views.flight_data, name='flight_data'),
    path('flight-delete/<int:pk>/', views.delete_flight, name='delete_flight'),
    path('manage-flight/<int:pk>/', views.flight_form, name="edit_flight"),
    path('create-flight/', views.add_flight2, name='add_flight2'),
    path('manage-reservations/', views.reservation_list, name='manage_reservations'),
    path('reservation-data/<int:pk>/', views.reservation_data, name='reservation_data'),
    path('reservation-edit/<int:pk>/', views.reservation_form, name='reservation_edit'),
    path('reservation-delete/<int:pk>/', views.delete_reservation, name='delete_reservation'),
    path('create-reservation/', views.add_reservation, name='add_reservation'),
    path('manage-passengers/', views.passenger_list, name='manage_passengers'),
    path('passenger-data/<int:pk>/', views.passenger_data, name='passenger_data'),
    path('passenger-edit/<int:pk>/', views.passenger_form, name='passenger_edit'),
    path('passenger-delete/<int:pk>/', views.delete_passenger, name='delete_passenger'),
    path('manage-staffs/', views.staff_list, name='manage_staff'),
    path('staff-data/<int:pk>/', views.staff_data, name='staff_data'),
    path('staff-edit/<int:pk>/', views.staff_form, name='staff_edit'),
    path('staff-delete/<int:pk>/', views.staff_delete, name='delete_staff'),
    path('add-staff/', views.add_staff, name='add_staff'),
]


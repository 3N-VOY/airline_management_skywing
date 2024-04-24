from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('manage-flights/', views.flight_list, name='manage_flight'),
    # path('', views.dashboard, name='dashboard'),
    # path('flights/', views.flight_list, name='flight_list'),
    path('flight-data/<int:pk>/', views.flight_data, name='flight_data'),
     
    # path('passengers/',views.passenger_list, name="passenger_list"),
    # path('staff/', views.view_staff, name="staff_view"),
    path('manage-flight/<int:pk>/', views.flight_form, name="edit_flight"),

]
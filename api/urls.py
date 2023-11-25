from django.urls import path
from . import views

# All endpoints are defined here

urlpatterns = [
  path('owner/', views.OwnerView.as_view(), name='owner'),
  path('animal/', views.AnimalView.as_view(), name='animal'),
  path('animal-service/', views.AnimalServiceView.as_view(), name='animal-service'),
  path('service/', views.ServiceView.as_view(), name='service'),
  path('vaccine/', views.VaccineView.as_view(), name='vaccine'),
  path('veterinary/', views.VeterinaryView.as_view(), name='veterinary'),
]
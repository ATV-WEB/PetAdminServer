from django.urls import path
from . import views

# All endpoints are defined here

urlpatterns = [
  path('owner/', views.OwnerView.as_view(), name='owner'), # Create (POST) and Read (GET) endpoints
  path('owner/<int:id>', views.OwnerEditView.as_view(), name='owner-edit'), # Edit (POST) and Read (GET) endpoints
  path('owner/delete/<int:id>', views.OwnerDeleteView.as_view(), name='owner-delete'), # Delete (GET) endpoint

  path('animal/', views.AnimalView.as_view(), name='animal'), # Create (POST) and Read (GET) endpoints
  path('animal/<int:id>', views.AnimalEditView.as_view(), name='animal-edit'), # Edit (POST) and Read (GET) endpoints
  path('animal/delete/<int:id>', views.AnimalDeleteView.as_view(), name='animal-delete'), # Delete (GET) endpoint

  path('animal-service/', views.AnimalServiceView.as_view(), name='animal-service'), # Create (POST) and Read (GET) endpoints
  path('animal-service/<int:id>', views.AnimalServiceEditView.as_view(), name='animal-service-edit'), # Edit (POST) and Read (GET) endpoints
  path('animal-service/delete/<int:id>', views.AnimalServiceDeleteView.as_view(), name='animal-service-delete'), # Delete (GET) endpoint

  path('service/', views.ServiceView.as_view(), name='service'), # Create (POST) and Read (GET) endpoints
  path('service/<int:id>', views.ServiceEditView.as_view(), name='service-edit'), # Edit (POST) and Read (GET) endpoints
  path('service/delete/<int:id>', views.ServiceDeleteView.as_view(), name='service-delete'), # Delete (GET) endpoint

  path('vaccine/', views.VaccineView.as_view(), name='vaccine'), # Create (POST) and Read (GET) endpoints
  path('vaccine/<int:id>', views.VaccineEditView.as_view(), name='vaccine-edit'), # Edit (POST) and Read (GET) endpoints
  path('vaccine/delete/<int:id>', views.VaccineDeleteView.as_view(), name='vaccine-delete'), # Delete (GET) endpoint

  path('veterinary/', views.VeterinaryView.as_view(), name='veterinary'), # Create (POST) and Read (GET) endpoints
  path('veterinary/<int:id>', views.VeterinaryEditView.as_view(), name='veterinary-edit'), # Edit (POST) and Read (GET) endpoints
  path('veterinary/delete/<int:id>', views.VeterinaryDeleteView.as_view(), name='veterinary-delete'), # Delete (GET) endpoint
]
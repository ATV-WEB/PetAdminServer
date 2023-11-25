from django.urls import path
from . import views

# All endpoints are defined here

urlpatterns = [
  path('owner/', views.OwnerView.as_view(), name='owner'),
  path('owner/<int:id>', views.OwnerEditView.as_view(), name='owner-edit'),
  path('owner/delete/<int:id>', views.OwnerDeleteView.as_view(), name='owner-delete'),
  path('animal/', views.AnimalView.as_view(), name='animal'),
  path('animal/<int:id>', views.AnimalEditView.as_view(), name='animal-edit'),
  path('animal/delete/<int:id>', views.AnimalDeleteView.as_view(), name='animal-delete'),
  path('animal-service/', views.AnimalServiceView.as_view(), name='animal-service'),
  path('animal-service/<int:id>', views.AnimalServiceEditView.as_view(), name='animal-service-edit'),
  path('animal-service/delete/<int:id>', views.AnimalServiceDeleteView.as_view(), name='animal-service-delete'),
  path('service/', views.ServiceView.as_view(), name='service'),
  path('vaccine/', views.VaccineView.as_view(), name='vaccine'),
  path('veterinary/', views.VeterinaryView.as_view(), name='veterinary'),
]
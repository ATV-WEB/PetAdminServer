from .serializers import OwnerSerializer, AnimalSerializer, AnimalServiceSerializer, ServiceSerializer, VaccineSerializer, VeterinarySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Owner, Animal, AnimalService, Service, Vaccine, Veterinary

class OwnerView(APIView): # endpoint for /api/owner
   def get(self, request, format=None):
    serializer = OwnerSerializer(Owner.objects.all(), many=True)
    return Response(serializer.data)

class AnimalView(APIView): # endpoint for /api/animal
  def get(self, request, format=None):
    serializer = AnimalSerializer(Animal.objects.all(), many=True)
    return Response(serializer.data)
  
class AnimalServiceView(APIView): # endpoint for /api/animal-service
  def get(self, request, format=None):
    serializer = AnimalServiceSerializer(AnimalService.objects.all(), many=True)
    return Response(serializer.data)
  
class ServiceView(APIView): # endpoint for /api/service
  def get(self, request, format=None):
    serializer = ServiceSerializer(Service.objects.all(), many=True)
    return Response(serializer.data)
  
class VaccineView(APIView): # endpoint for /api/vaccine
  def get(self, request, format=None):
    serializer = VaccineSerializer(Vaccine.objects.all(), many=True)

    return Response(serializer.data)
  
class VeterinaryView(APIView): # endpoint for /api/veterinary
  def get(self, request, format=None):
    serializer = VeterinarySerializer(Veterinary.objects.all(), many=True)
    return Response(serializer.data)
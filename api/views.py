from . import serializers
from rest_framework.views import APIView
from .models import Owner, Animal, AnimalService, Service, Vaccine, Veterinary
from django.http import JsonResponse

class OwnerView(APIView): # endpoint for /api/owner
   def get(self, request, format=None):
    serializer = serializers.OwnerSerializer(Owner.objects.all(), many=True)
    return JsonResponse(data=serializer.data, status=200, safe=False)
   
   def post(self, request, format=None):
      serializer = serializers.OwnerSerializer(data=request.data)

      if serializer.is_valid():
        serializer.save()
        return JsonResponse(data=serializer.data, status=201)
      
      return JsonResponse(data=serializer.errors, status=400)
   
class OwnerEditView(APIView): # endpoint for /api/owner/<id>
  def get(self, request, id, format=None):
    serializer = serializers.OwnerSerializer(Owner.objects.get(id=id))
    return JsonResponse(data=serializer.data, status=200, safe=False)
  
  def post(self, request, id, format=None):
    serializer = serializers.OwnerSerializer(Owner.objects.get(id=id), data=request.data)

    if serializer.is_valid():
      serializer.save()
      return JsonResponse(data=serializer.data, status=201)

    return JsonResponse(data=serializer.errors, status=400)
  
class OwnerDeleteView(APIView): # endpoint for /api/owner/delete/<id>
  def get(self, request, id, format=None):
    data = Owner.objects.get(id=id)
    data.delete()
    return JsonResponse(data={'delete' : 'okay'}, status=200, safe=False)

class AnimalView(APIView): # endpoint for /api/animal
  def get(self, request, format=None):
    serializer = serializers.AnimalSerializer(Animal.objects.all(), many=True)
    return JsonResponse(data=serializer.data, status=200, safe=False)

  def post(self, request, format=None):
    serializer = serializers.AnimalSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return JsonResponse(data=serializer.data, status=201)

    return JsonResponse(data=serializer.errors, status=400)
  
class AnimalEditView(APIView): # endpoint for /api/animal/<id>
  def get(self, request, id, format=None):
    serializer = serializers.AnimalSerializer(Animal.objects.get(id=id))
    return JsonResponse(data=serializer.data, status=200, safe=False)
  
  def post(self, request, id, format=None):
    serializer = serializers.AnimalSerializer(Animal.objects.get(id=id), data=request.data)

    if serializer.is_valid():
      serializer.save()
      return JsonResponse(data=serializer.data, status=201)

    return JsonResponse(data=serializer.errors, status=400)
  
class AnimalDeleteView(APIView): # endpoint for /api/animal/delete/<id>
  def get(self, request, id, format=None):
    data = Animal.objects.get(id=id)
    data.delete()
    return JsonResponse(data={'delete' : 'okay'}, status=200, safe=False)

class AnimalServiceView(APIView): # endpoint for /api/animal-service
  def get(self, request, format=None):
    serializer = serializers.AnimalServiceSerializer(AnimalService.objects.all(), many=True)
    return JsonResponse(data=serializer.data, status=200, safe=False)

  def post(self, request, format=None):
    serializer = serializers.AnimalServiceSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return JsonResponse(data=serializer.data, status=201)

    return JsonResponse(data=serializer.errors, status=400)
  
class AnimalServiceEditView(APIView): # endpoint for /api/animal-service/<id>
  def get(self, request, id, format=None):
    serializer = serializers.AnimalServiceSerializer(AnimalService.objects.get(id=id))
    return JsonResponse(data=serializer.data, status=200, safe=False)
  
  def post(self, request, id, format=None):
    serializer = serializers.AnimalServiceSerializer(AnimalService.objects.get(id=id), data=request.data)

    if serializer.is_valid():
      serializer.save()
      return JsonResponse(data=serializer.data, status=201)

    return JsonResponse(data=serializer.errors, status=400)
  
class AnimalServiceDeleteView(APIView): # endpoint for /api/animal-service/delete/<id>
  def get(self, request, id, format=None):
    data = AnimalService.objects.get(id=id)
    data.delete()
    return JsonResponse(data={'delete' : 'okay'}, status=200, safe=False)
  
class ServiceView(APIView): # endpoint for /api/service
  def get(self, request, format=None):
    serializer = serializers.ServiceSerializer(Service.objects.all(), many=True)
    return JsonResponse(data=serializer.data, status=200, safe=False)

  def post(self, request, format=None):
    serializer = serializers.ServiceSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return JsonResponse(data=serializer.data, status=201)

    return JsonResponse(data=serializer.errors, status=400)
  
class ServiceEditView(APIView): # endpoint for /api/service/<id>
  def get(self, request, id, format=None):
    serializer = serializers.ServiceSerializer(Service.objects.get(id=id))
    return JsonResponse(data=serializer.data, status=200, safe=False)
  
  def post(self, request, id, format=None):
    serializer = serializers.ServiceSerializer(Service.objects.get(id=id), data=request.data)

    if serializer.is_valid():
      serializer.save()
      return JsonResponse(data=serializer.data, status=201)

    return JsonResponse(data=serializer.errors, status=400)

class ServiceDeleteView(APIView): # endpoint for /api/service/delete/<id>
  def get(self, request, id, format=None):
    data = Service.objects.get(id=id)
    data.delete()
    return JsonResponse(data={'delete' : 'okay'}, status=200, safe=False)
  
class VaccineView(APIView): # endpoint for /api/vaccine
  def get(self, request, format=None):
    serializer = serializers.VaccineSerializer(Vaccine.objects.all(), many=True)

    return JsonResponse(data=serializer.data, status=200, safe=False)

  def post(self, request, format=None):
    serializer = serializers.VaccineSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return JsonResponse(data=serializer.data, status=201)

    return JsonResponse(data=serializer.errors, status=400)
  
class VaccineEditView(APIView): # endpoint for /api/vaccine/<id>
  def get(self, request, id, format=None):
    serializer = serializers.VaccineSerializer(Vaccine.objects.get(id=id))
    return JsonResponse(data=serializer.data, status=200, safe=False)
  
  def post(self, request, id, format=None):
    serializer = serializers.VaccineSerializer(Vaccine.objects.get(id=id), data=request.data)

    if serializer.is_valid():
      serializer.save()
      return JsonResponse(data=serializer.data, status=201)

    return JsonResponse(data=serializer.errors, status=400)

class VaccineDeleteView(APIView): # endpoint for /api/vaccine/delete/<id>
  def get(self, request, id, format=None):
    data = Vaccine.objects.get(id=id)
    data.delete()
    return JsonResponse(data={'delete' : 'okay'}, status=200, safe=False)
  
class VeterinaryView(APIView): # endpoint for /api/veterinary
  def get(self, request, format=None):
    serializer = serializers.VeterinarySerializer(Veterinary.objects.all(), many=True)
    return JsonResponse(data=serializer.data, status=200, safe=False)

  def post(self, request, format=None):
    serializer = serializers.VeterinarySerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return JsonResponse(data=serializer.data, status=201)

    return JsonResponse(data=serializer.errors, status=400)
  
class VeterinaryEditView(APIView): # endpoint for /api/veterinary/<id>
  def get(self, request, id, format=None):
    serializer = serializers.VeterinarySerializer(Veterinary.objects.get(id=id))
    return JsonResponse(data=serializer.data, status=200, safe=False)
  
  def post(self, request, id, format=None):
    serializer = serializers.VeterinarySerializer(Veterinary.objects.get(id=id), data=request.data)

    if serializer.is_valid():
      serializer.save()
      return JsonResponse(data=serializer.data, status=201)

    return JsonResponse(data=serializer.errors, status=400)
  
class VeterinaryDeleteView(APIView): # endpoint for /api/veterinary/delete/<id>
  def get(self, request, id, format=None):
    data = Veterinary.objects.get(id=id)
    data.delete()
    return JsonResponse(data={'delete' : 'okay'}, status=200, safe=False)
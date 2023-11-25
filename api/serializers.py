from rest_framework import serializers
from .models import Owner, Animal, AnimalService, Service, Vaccine, Veterinary

class OwnerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Owner
    fields = ['id', 'name', 'address', 'email']

class AnimalSerializer(serializers.ModelSerializer):
  class Meta:
    model = Animal
    fields = ['id', 'name', 'breed', 'age', 'gender', 'owner', 'vaccines', 'services']

class AnimalServiceSerializer(serializers.ModelSerializer):
  class Meta:
    model = AnimalService
    fields = ['id', 'animal', 'service', 'veterinary', 'date']

class ServiceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Service
    fields = ['id',  'name', 'schedule_start', 'schedule_end', 'price', 'veterinary']

class VaccineSerializer(serializers.ModelSerializer):
  class Meta:
    model = Vaccine
    fields = ['id', 'name', 'date']

class VeterinarySerializer(serializers.ModelSerializer):
  class Meta:
    model = Veterinary
    fields = ['id', 'name', 'specialty']
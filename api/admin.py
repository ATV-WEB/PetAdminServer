from django.contrib import admin
from .models import Owner, Animal, Service, Vaccine, Veterinary, AnimalService

# Registering my models in the admin site with the decorator
admin.register(Owner, Animal, Service, Vaccine, Veterinary, AnimalService)(admin.ModelAdmin)
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal

# OS = Ordem de Serviço (Service Order)

class Owner(models.Model):
  name = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  email = models.CharField(max_length=255, unique=True)

  def __str__(self):
    return f'{self.name}'

class Animal(models.Model):
  name = models.CharField(max_length=255)
  breed = models.CharField(max_length=255)
  age = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
  gender = models.CharField(max_length=1, choices=[('m', 'masculino'), ('f', 'feminino')])
  owners = models.ManyToManyField('Owner')
  vaccines = models.ManyToManyField('Vaccine', blank=True)
  services = models.ManyToManyField('Service', through='OS', blank=True)

  def __str__(self):
    return f'{self.name}'
  
# This is the model that represents the relationship N:N between Animal and Service
class OS(models.Model):
  name = models.CharField(max_length=255)
  animal = models.ForeignKey('Animal', on_delete=models.CASCADE)
  service = models.ForeignKey('Service', on_delete=models.CASCADE)
  schedule_start = models.DateTimeField()
  schedule_end = models.DateTimeField()

  def __str__(self):
    return f'{self.animal} - {self.service}'

class Service(models.Model):
  name = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=15, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
  veterinary = models.ForeignKey('Veterinary', on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.name}'

class Vaccine(models.Model):
  name = models.CharField(max_length=255)
  date = models.DateField()

  def __str__(self):
    return f'{self.name}'
  
class Veterinary(models.Model):
  name = models.CharField(max_length=255)
  specialty = models.CharField(max_length=255)

  def __str__(self):
    return f'{self.name}'

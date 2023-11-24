from django.db import models

class Owner(models.Model):
  name = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  email = models.CharField(max_length=255)

  def __str__(self):
    return self.name

class Animal(models.Model):
  name = models.CharField(max_length=255)
  breed = models.CharField(max_length=255)
  age = models.IntegerField()
  gender = models.CharField(max_length=255, choices=[('m', 'masculino'), ('f', 'femenino')], default='m')
  owner = models.ManyToManyField('Owner')
  vaccines = models.ManyToManyField('Vaccine', blank=True)
  services = models.ManyToManyField('Service', through='AnimalService', blank=True)

  def __str__(self):
    return self.name

# This is the model that represents the relationship N:M between Animal, Service and Veterinary
class AnimalService(models.Model):
  animal = models.ForeignKey('Animal', on_delete=models.CASCADE)
  service = models.ForeignKey('Service', on_delete=models.CASCADE)
  veterinary = models.ForeignKey('Veterinary', on_delete=models.CASCADE)
  date = models.DateTimeField()

  def __str__(self):
    return self.animal.name + ' - ' + self.service.name

class Service(models.Model):
  name = models.CharField(max_length=255)
  schedule_start = models.TimeField()
  schedule_end = models.TimeField()
  price = models.IntegerField()
  veterinary = models.ForeignKey('Veterinary', on_delete=models.CASCADE)

  def __str__(self):
    return self.name

class Vaccine(models.Model):
  name = models.CharField(max_length=255)
  date = models.DateField()

  def __str__(self):
    return self.name
  
class Veterinary(models.Model):
  name = models.CharField(max_length=255)
  specialty = models.CharField(max_length=255)

  def __str__(self):
    return self.name

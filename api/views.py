from django.contrib.auth.models import User # Temporary Model
from .serializers import UserSerializer
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet): # Endpoint for /users
  queryset = User.objects.all()
  serializer_class = UserSerializer

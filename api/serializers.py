from django.contrib.auth.models import User # Temporary Model
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer): # Jsonify the User Model
  class Meta:
    model = User
    fields = ['id', 'username', 'email']
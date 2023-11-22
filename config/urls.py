from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
  path('api/', include(router.urls), name='api'),
  path('admin/', admin.site.urls, name='admin'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('', include('pages.urls'), name='pages'),
  path('api/', include('api.urls'), name='api'),
  path('admin/', admin.site.urls, name='admin'),
]

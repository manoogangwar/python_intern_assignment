from django.shortcuts import render
from rest_framework import viewsets
from .models import App
from .Serializers import AppSerializer

# Create your views here.
class AppViewSet(viewsets.ModelViewSet):
    queryset= App.objects.all()
    serializer_class=AppSerializer

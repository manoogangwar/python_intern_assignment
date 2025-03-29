from django.contrib import admin
from django.urls import path,include
from .views import AppViewSet
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r'Apps', AppViewSet)

urlpatterns = [    
    path('',include(router.urls))
      
]


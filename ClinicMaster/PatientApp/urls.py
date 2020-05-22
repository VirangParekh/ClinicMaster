#from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import *

router=DefaultRouter()
router.register(r"profile",viewset=PatientProfileView)

urlpatterns=[

] + router.urls
#from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import *

router=DefaultRouter()
router.register(r"doctor_profile",viewset=DoctorProfileView)
router.register(r"prescription", viewset=PrescrptionView)
router.register(r"appointment",viewset=AppointmentView)

urlpatterns=[

] + router.urls
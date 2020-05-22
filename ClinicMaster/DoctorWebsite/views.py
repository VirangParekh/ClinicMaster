from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *


class DoctorProfileView(ModelViewSet):
    serializer_class=DoctorProfileSerializer
    queryset=DoctorModel.objects.all()

class PrescrptionView(ModelViewSet):
    serializer_class=PrescriptionSerializer
    queryset=Prescription.objects.all()

class AppointmentView(ModelViewSet):
    serializer_class=AppointmentSerializer
    queryset=Appointment.objects.all()



# Create your views here.

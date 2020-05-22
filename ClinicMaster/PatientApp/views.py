from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *

class PatientProfileView(ModelViewSet):
    serializer_class=PatientProfileSerializer
    queryset=PatientModel.objects.all()

# Create your views here.

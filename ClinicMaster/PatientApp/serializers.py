from rest_framework.serializers import ModelSerializer as msr
from .models import *
from DoctorWebsite.models import *


class PatientProfileSerializer(msr):
    class Meta:
        model=PatientModel
        fields='__all__'
        read_only_fields=['user']

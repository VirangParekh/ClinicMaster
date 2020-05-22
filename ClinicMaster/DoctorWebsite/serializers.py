from rest_framework.serializers import ModelSerializer as msr
from .models import *
from rest_framework import serializers

class DoctorProfileSerializer(msr):

    class Meta:
        model=DoctorModel
        fields='__all__'
        read_only_fields=['user']


class MedicineSerializer(msr):
    class Meta:
        model=Medicine
        exclude=['patient']

class PrescriptionSerializer(msr):
    medicine=MedicineSerializer(many=False, allow_null=True)
    class Meta:
        model=Prescription
        fields='__all__'
        read_only_fields=['doctor']

class AppointmentSerializer(msr):
    class Meta:
        model=Appointment
        fields='__all__'
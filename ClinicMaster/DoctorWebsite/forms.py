from django.forms import ModelForm as mf
from .models import Clinic, DoctorModel, Medicine, Prescription, Appointment

class ClinicForm(mf):
    class Meta:
        model= Clinic
        fields='__all__'

class DoctorForm(mf):
    class Meta:
        model=DoctorModel
        fields='__all__'
        excluded=[
            'user'
        ]

class Medicine(mf):  #instanciate without fail
    class Meta:
        model=Medicine
        fields='__all__'
        excluded=[
            'patient',
        ]

class Appointment(mf):
    class Meta:
        model= Appointment
        fields='__all__'
        excluded=[
            'patient',
            'doctor',
        ]



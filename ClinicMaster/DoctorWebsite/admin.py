from django.contrib import admin
from .models import *

admin.register(DoctorModel)
admin.register(Clinic)
admin.register(Medicine)
admin.register(Prescription)
admin.register(Appointment)

# Register your models here.

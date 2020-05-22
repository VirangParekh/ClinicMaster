from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
#from DoctorWebsite.models import Prescription

class PatientModel(models.Model):
    weight_unit_choices=(
        ('Kilograms', 'kg'),
        ('Pounds', 'lbs'),
    )
    height_unit_choices=(
        ('metres','mts'),
        ('feet','ft'),
    )
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(verbose_name='Name of the Patient', max_length=250)
    age=models.IntegerField(verbose_name='age of the pathient', validators=[MinValueValidator(0, message='please enter a valid age')])
    last_visit=models.DateField(verbose_name='Last Visit')
    next_visit=models.DateField(verbose_name='Next Visit')
    bp_sys=models.IntegerField(verbose_name='Systolic Blood Pressure')
    bp_dia=models.IntegerField(verbose_name='Diastolic Blood Pressure')
    bmi=models.FloatField(verbose_name='Body Mass Index')
    weight=models.FloatField(verbose_name='weight')
    height=models.FloatField(verbose_name='height')
    weight_unit=models.CharField(verbose_name='Unit of Weight', choices=weight_unit_choices, max_length=12)
    height_unit=models.CharField(verbose_name='Unit f Height', choices=height_unit_choices, max_length=12)
    medical_history=models.FileField(verbose_name='Medical History')
    #prescription=models.ForeignKey(Prescription, related_name='patient')

    def __str__(self):
        return self.name
# Create your models here.

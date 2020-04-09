from django.db import models
from django.contrib.auth.models import User
from PatientApp.models import PatientModel
from django.core.validators import MinValueValidator
import templates.DoctorWebsite.Images

class Clinic(models.Model):
    #doctor=models.ManyToManyField(DoctorModel, related_name='clinic')
    name=models.CharField(verbose_name='clinic_name', max_length=200)
    from_time=models.TimeField(verbose_name='from_time')
    to_time=models.TimeField(verbose_name='to_time')
    days=models.CharField(verbose_name='working_days', max_length=300, default='Open all days')

    def __str__(self):
        return self.name

class DoctorModel(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    first_name=models.CharField(verbose_name='first_name',max_length=150)
    last_name=models.CharField(verbose_name='last_name',max_length=150)
    phone_personal=models.CharField(verbose_name='number_own', max_length=12)
    degree=models.CharField(verbose_name='degree', max_length=120)
    description=models.CharField(verbose_name='description', max_length=500)
    experience=models.IntegerField(verbose_name='experience')
    practice_number=models.CharField(verbose_name='practice_number', max_length=7)
    clinic=models.ManyToManyField(Clinic, related_name='doctor')
    photo=models.ImageField(verbose_name='doctor_photo', upload_to='Images')

    def __str__(self):
        return '%s %s'%(self.first_name,self.last_name)


class Medicine(models.Model):
    mode_choices=(
        ('Advice','Advice'),
        ('Medicine','Medicine'),

    )
    patient=models.ForeignKey(PatientModel, on_delete=models.CASCADE)
    mode=models.CharField(verbose_name='mode',choices=mode_choices, max_length=8)
    description=models.CharField(verbose_name='medicine_description',max_length=500)
    morning=models.IntegerField(verbose_name='medicine_in_morning', validators=[MinValueValidator(0, message='Number of medicines cannot be negative')])
    afternoon=models.IntegerField(verbose_name='medicine_in_afternoon', validators=[MinValueValidator(0, message='Number of medicines cannot be negative')])
    evening=models.IntegerField(verbose_name='medicine_in_evening', validators=[MinValueValidator(0, message='Number of medicines cannot be negative')])
    days=models.IntegerField(verbose_name='number_of_days', validators=[MinValueValidator(0, message='Number of days cannot be negative')])
    
    def __str__(self):
        return '%s %s %s-%s-%s %s'%(self.mode,self.description,str(self.morning),str(self.afternoon),str(self.evening),str(self.days))

class Prescription(models.Model):
    patient=models.ForeignKey(PatientModel, on_delete=models.CASCADE)
    medicine=models.ForeignKey(Medicine, on_delete=models.CASCADE)

class Appointment(models.Model):
    patient= models.ForeignKey(PatientModel, on_delete=models.CASCADE)
    doctor=models.ForeignKey(DoctorModel, on_delete=models.CASCADE)
    time=models.TimeField(verbose_name='appointment_time')
    date=models.TimeField(verbose_name='appointment_date')


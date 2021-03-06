# Generated by Django 3.0.4 on 2020-05-22 09:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name of the Patient')),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message='please enter a valid age')], verbose_name='age of the pathient')),
                ('last_visit', models.DateField(verbose_name='Last Visit')),
                ('next_visit', models.DateField(verbose_name='Next Visit')),
                ('bp_sys', models.IntegerField(verbose_name='Systolic Blood Pressure')),
                ('bp_dia', models.IntegerField(verbose_name='Diastolic Blood Pressure')),
                ('bmi', models.FloatField(verbose_name='Body Mass Index')),
                ('weight', models.FloatField(verbose_name='weight')),
                ('height', models.FloatField(verbose_name='height')),
                ('weight_unit', models.CharField(choices=[('Kilograms', 'kg'), ('Pounds', 'lbs')], max_length=12, verbose_name='Unit of Weight')),
                ('height_unit', models.CharField(choices=[('metres', 'mts'), ('feet', 'ft')], max_length=12, verbose_name='Unit f Height')),
                ('medical_history', models.FileField(upload_to='', verbose_name='Medical History')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

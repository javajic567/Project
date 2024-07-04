from django.db import models
from doctor_app import models as m
# Create your models here.
class Patient(models.Model):
    patient_name=models.CharField(max_length=80)
    patient_age=models.CharField(max_length=80)
    patient_email=models.EmailField()
    appointment_cause=models.CharField(max_length=50)
    appointment_date=models.CharField(max_length=1000)

    def __str__(self):
        return self.patient_name
    doctor=models.ForeignKey(m.Doctor_details,on_delete=models.CASCADE)

from django.db import models

# Create your models here.
class Doctor_details(models.Model):
    name=models.CharField(max_length=50)
    specilazion=models.CharField(max_length=50)
    expirence=models.CharField(max_length=50)
    joining_date=models.DateField()

    def __str__(self):
        return self.name

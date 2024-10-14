from django.db import models
from patients.models import Patient
import pytz

# Create your models here.
class Illness(models.Model):
    illness_name = models.CharField(max_length=255)

    def __str__(self):
        return self.illness_name


class Records(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    date_added = models.DateField(auto_now_add=True)
    checkup_details = models.TextField()
    illness = models.ForeignKey(Illness, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.patient.first_name} {self.patient.last_name}"
    




from django.db import models
from patients.models import Patient
import pytz

# Create your models here.
class Records(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    date_added = models.DateField(auto_now_add=True)
    checkup_details = models.TextField()

    def __str__(self):
        return f"{self.patient.first_name} {self.patient.last_name}"




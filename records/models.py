from django.db import models
from patients.models import Patient
from users.models import User

# Create your models here.
class Records(models.Model):
    patient = models.ManyToManyField(Patient, related_name="patient_records")
    date_added = models.DateField(auto_created=True)
    checkup_details = models.TextField()
    added_by = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)



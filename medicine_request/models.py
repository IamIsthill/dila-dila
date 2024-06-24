from django.db import models
from patients.models import Patient

# Create your models here.
class Request(models.Model):
    requester = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    date_requested = models.DateTimeField(auto_now=True)
    date_fulfilled = models.DateTimeField(null=True)
    medicine = models.CharField(max_length=255, null=False)
    quantity = models.PositiveIntegerField(null=False)

    def __str__(self):
        name = f'{self.requester.first_name} {self.requester.last_name} - {self.medicine}'
        return name
    
    class Meta:
        ordering=['-date_requested']


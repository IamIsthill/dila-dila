from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=100, null=False )
    last_name = models.CharField(max_length=100, null=False )
    DOB = models.DateField(null=False)
    address = models.CharField(max_length=255)
    contact = models.TextField()
    added = models.DateTimeField(auto_now=True, editable=True)

    def __str__(self):
        text = f'{self.first_name} {self.last_name}'
        return text 
    
    class Meta:
        ordering = ['-added']
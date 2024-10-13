from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=100, null=True )
    middle_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True )
    suffix = models.CharField(max_length=20, null=True)
    maiden_name = models.CharField(max_length=100, null=True)
    sex = models.CharField(max_length=10, null=True)
    mother_name = models.CharField(max_length=100, null=True)

    DOB = models.DateField(null=False)
    blood_type = models.CharField(max_length=20, null=True)
    civil_status = models.CharField(max_length=20, null=True)
    is_nhts = models.BooleanField(default=True)
    spouse_name = models.CharField(max_length=50, null=True)
    facility_household_no = models.IntegerField(null=True)
    education = models.CharField(max_length=40, null=True)
    is_4ps = models.BooleanField(default=False)

    household_no = models.IntegerField(null=True)
    is_philhealth = models.BooleanField(default=False)
    status_type = models.CharField(max_length=20, null=True)
    philhealth_no = models.IntegerField(null=True)
    member_type = models.CharField(max_length=50, null=True)
    is_pcb = models.BooleanField(default=False)

    employment_status = models.CharField(max_length=20, null=True)
    family_member = models.CharField(max_length=20, null=True)



    contact = models.IntegerField()
    address = models.CharField(max_length=255)
    added = models.DateTimeField(auto_now=True, editable=True)

    def __str__(self):
        text = f'{self.first_name} {self.last_name}'
        return text 
    
    class Meta:
        ordering = ['-added']
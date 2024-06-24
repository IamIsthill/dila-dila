from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'DOB', 'address', 'contact', 'added')

admin.site.register(Patient, PatientAdmin)

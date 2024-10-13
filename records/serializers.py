from rest_framework import serializers
from .models import Records
from patients.models import Patient

class RecordSerializer(serializers.ModelSerializer):
    patient_first_name = serializers.CharField(
        source = "patient.first_name", read_only=True
    )
    patient_last_name = serializers.CharField(
        source = "patient.last_name", read_only=True
    )
    class Meta:
        model = Records
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

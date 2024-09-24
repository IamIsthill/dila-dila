from rest_framework import serializers
from .models import Records

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

from django.forms import ModelForm
from django import forms
from patients.models import Patient
from . models import Request


class RequestForm(ModelForm):
    requester = forms.ModelChoiceField(queryset=Patient.objects.all(), empty_label="Select Patient")
    class Meta:
        model = Request
        fields = '__all__'
from django.forms import ModelForm
from django import forms
from .models import Patient
import logging

logger = logging.getLogger(__name__)

class PatientForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=False)
    middle_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    suffix = forms.CharField(max_length=20,required=False)

    sex = forms.CharField(max_length=10, required=False)
    blood_type = forms.CharField(max_length=20, required=False)
    DOB = forms.DateField(required=False)
    civil_status = forms.CharField(max_length=20, required=False)
    birth_place = forms.CharField(max_length=100, required=False)
    contact = forms.IntegerField(required=False)
    maiden_name = forms.CharField(max_length=100, required=False)

    address = forms.CharField(max_length=255, required=False)
    spouse_name = forms.CharField(max_length=50, required=False)
    mother_name = forms.CharField(max_length=100, required=False)
    family_member = forms.CharField(max_length=20, required=False)

    education = forms.CharField(max_length=40, required=False)
    employment_status = forms.CharField(max_length=20, required=False)

    is_nhts = forms.CharField(max_length=5, required=False)
    facility_household_no = forms.IntegerField(required=False)

    is_4ps = forms.CharField(max_length=5, required=False)
    household_no = forms.IntegerField(required=False)

    is_philhealth = forms.CharField(max_length=5, required=False)
    status_type = forms.CharField(max_length=20, required=False)
    philhealth_no = forms.IntegerField(required=False)
    member_category = forms.CharField(max_length=50, required=False)
    is_pcb = forms.CharField(max_length=5, required=False)

    def save(self):
        first_name = self.cleaned_data.get('first_name')
        middle_name = self.cleaned_data.get('middle_name')
        last_name = self.cleaned_data.get('last_name')
        suffix = self.cleaned_data.get('suffix')

        sex = self.cleaned_data.get('sex')
        blood_type = self.cleaned_data.get('blood_type')
        DOB = self.cleaned_data.get('DOB')
        civil_status = self.cleaned_data.get('civil_status')
        birth_place = self.cleaned_data.get('birth_place')
        contact =self.cleaned_data.get('contact')
        maiden_name = self.cleaned_data.get('maiden_name')

        address = self.cleaned_data.get('address')
        spouse_name = self.cleaned_data.get('spouse_name')
        mother_name = self.cleaned_data.get('mother_name')
        family_member = self.cleaned_data.get('family_member')

        education = self.cleaned_data.get('education')
        employment_status = self.cleaned_data.get('employment_status')

        is_nhts = self.cleaned_data.get('is_nhts')
        facility_household_no =self.cleaned_data.get('facility_household_no')

        is_4ps = self.cleaned_data.get('is_4ps')
        household_no =self.cleaned_data.get('household_no')

        is_philhealth = self.cleaned_data.get('is_philhealth')
        status_type = self.cleaned_data.get('status_type')
        philhealth_no = self.cleaned_data.get('philhealth_no')
        member_category = self.cleaned_data.get('member_category')
        is_pcb = self.cleaned_data.get('is_pcb')

        try:
            patient = Patient.objects.create(
                first_name = first_name,
                last_name = last_name,
                middle_name = middle_name,
                blood_type = blood_type,
                DOB = DOB,
                sex = sex,
                civil_status = civil_status,
                birth_place = birth_place,
                contact=contact,

                address = address,
                spouse_name = spouse_name,
                mother_name = mother_name,
                family_member = family_member,
                education = education,
                employment_status = employment_status
            )

            

            if sex.lower() == 'female':
                patient.maiden_name = maiden_name

            
            if is_nhts.lower() == 'yes':
                patient.is_nhts = True
                patient.facility_household_no = facility_household_no
            else:
                patient.is_nhts = False
            
            if is_4ps.lower() == 'yes':
                patient.is_4ps = True
                patient.household_no = household_no
            else:
                patient.is_4ps = False
            
            if is_philhealth.lower() == 'yes':
                patient.is_philhealth = True
                patient.philhealth_no = philhealth_no
                patient.status_type = status_type

                if status_type.lower() == 'member':
                    patient.member_category = member_category
            else:
                patient.is_philhealth = False
            
            if is_pcb.lower() == 'yes':
                patient.is_pcb = True
            else:
                patient.is_pcb = False
            
            patient.save()

        except Exception as e:
            logger.error(f'{str(e)}')



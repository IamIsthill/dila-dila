from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PatientForm
from .models import Patient
from medicine_request.models import Request
from records.models import Records
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import logging

logger = logging.getLogger(__name__)

# Create your views here.
@login_required(login_url='login')
def add_patient_view(request):
    form =PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient successfully added')
            return redirect('patient-list')
        else:
            print(form.errors)
            messages.error(request, 'Error adding the patient')
        referrer = request.META.get("HTTP_REFERER")
        if referrer:
            return redirect(referrer)
        else:
            return redirect('patient-list')
    return render(request, 'patients/add_patient.html')

@login_required(login_url='login')
def patient_list(request):
    q = request.GET.get('search') if request.GET.get('search') != None else ''
    patients = Patient.objects.filter(
        Q(first_name__icontains=q)|Q(last_name__icontains=q)
    )
    paginator = Paginator(patients, 5)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    context = {'patients':patients, 'items':items}
    return render(request, 'patients/patients.html', context)

@login_required(login_url='login')
def edit_patient_view(request, pk):
    patient = Patient.objects.get(id=pk)
    if request.method == 'POST':
        patient.first_name = request.POST.get('first_name')
        patient.middle_name = request.POST.get('middle_name')
        patient.last_name = request.POST.get('last_name')
        patient.suffix = request.POST.get('suffix')

        patient.DOB = request.POST.get('DOB')
        patient.address = request.POST.get('address')
        patient.sex = request.POST.get('sex')
        patient.blood_type = request.POST.get('blood_type')
        patient.civil_status = request.POST.get('civil_status')
        patient.birth_place = request.POST.get('birth_place')
        patient.contact = request.POST.get('contact')
        patient.spouse_name = request.POST.get('spouse_name')
        patient.mother_name = request.POST.get('mother_name')
        patient.family_member = request.POST.get('family_member')
        patient.education = request.POST.get('education')
        patient.employment_status = request.POST.get('employment_status')

        if request.POST.get('sex') == 'Female':
            patient.maiden_name = request.POST.get('maiden_name')
        else:
            patient.maiden_name = ''

        if request.POST.get('is_nhts') == 'yes':
            patient.is_nhts = True
            patient.facility_household_no = request.POST.get('facility_household_no')
        else:
            patient.is_nhts = False

        if request.POST.get('is_4ps') == 'yes':
            patient.is_4ps = True
            patient.household_no = request.POST.get('household_no')
        else:
            patient.is_4ps = False

        if request.POST.get('is_philhealth') == 'yes':
            patient.is_philhealth = True
            patient.philhealth_no = request.POST.get('philhealth_no')
            patient.status_type = request.POST.get('status_type')

            if request.POST.get('status_type') == 'Member':
                patient.member_category = request.POST.get('member_category')
        else:
            patient.is_philhealth = False
        
        if request.POST.get('is_pcd') == 'yes':
            patient.is_pcb = True
        else:
            patient.is_pcb = False
        
        try:
            patient.save()
            messages.success(request, 'Patient successfully updated.')

        except Exception as e:
            logger.error(f'{str(e)}')
            messages.error(request, 'Failed to update patient data.')
        return redirect('patient-list')
    context = {'patient':patient}
    return render(request, 'patients/edit_patient.html', context)

@login_required(login_url='login')
def delete_patient_view(request, pk):
    patient = Patient.objects.get(id=pk)
    if request.method == 'POST':
        patient.delete()
        messages.success(request, "Patient deleted successfully.")
        return redirect('patient-list')
    context = {'patient': patient}
    return render(request, 'patients/delete_patient.html', context)

@login_required(login_url='login')
def patient(request, pk):
    patient = Patient.objects.get(id=pk)
    requests = Request.objects.filter(requester = patient)
    paginator = Paginator(requests, 5)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    context = {'patient':patient, 'requests': requests, 'items':items}
    return render(request, 'patients/patient.html', context)


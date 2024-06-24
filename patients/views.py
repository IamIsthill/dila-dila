from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PatientForm
from .models import Patient
from medicine_request.models import Request
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
            messages.error(request, 'Error adding the patient')
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
        patient.last_name = request.POST.get('last_name')
        patient.DOB = request.POST.get('DOB')
        patient.address = request.POST.get('address')
        patient.contact = request.POST.get('contact')
        patient.save()
        messages.success(request, 'Patient successfully updated.')
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


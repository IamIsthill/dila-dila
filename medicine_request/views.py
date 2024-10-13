from django.shortcuts import render, redirect, get_object_or_404
from patients.models import Patient
from .models import Request
from .forms import RequestForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
@login_required(login_url='login')
def add_request_view(request):
    patients = Patient.objects.all()
    form = RequestForm()
    if request.method == 'POST':
        try:
            pk = request.POST.get('requester')
            if not pk:
                raise ValueError("Patient ID (pk) is required.")
            patient = get_object_or_404(Patient, id=int(pk))
            med = Request.objects.create(
                requester=patient,
                medicine=request.POST.get('medicine'),
                quantity=request.POST.get('quantity')
            )
            messages.success(request, 'Request successfully added')
            return redirect('request', med.id)
        except (ValueError, Patient.DoesNotExist):
            messages.error(request, 'Patient not found or invalid request. Please ensure that the patient is already added.')
    context = {'patients': patients, 'form': form}
    return render(request, 'medicine_request/add-request.html', context)

@login_required(login_url='login')
def request_view(request, pk):
    medreq = Request.objects.get(id=pk)
    context = {'medreq': medreq}
    return render(request, 'medicine_request/request.html', context)

@login_required(login_url='login')
def request_toggle(request, pk):
    medreq = Request.objects.get(id=pk)
    if medreq.date_fulfilled is None:
        medreq.date_fulfilled = datetime.now()
    else:
        medreq.date_fulfilled = None
    medreq.save()
    return redirect('request', medreq.id)

@login_required(login_url='login')
def update_request_view(request, pk):
    medreq = Request.objects.get(id=pk)
    if request.method == 'POST':
        try:
            medreq.medicine = request.POST.get('medicine')
            medreq.quantity = request.POST.get('quantity')
            medreq.date_fulfilled = None
            medreq.save()
            messages.success(request, 'Request updated successfully.')
            return redirect('request', medreq.id)
            
        except:
            messages.error(request, 'Failed to update the request.')
    context={'medreq':medreq}
    return render(request, 'medicine_request/update-request.html', context)

@login_required(login_url='login')
def delete_request_view(request, pk):
    medreq = Request.objects.get(id=pk)
    if request.method == 'POST':
        medreq.delete()
        messages.success(request, 'Request successfully deleted.')
        return redirect('request-list')
    context = {'medreq':medreq}
    return render(request, 'medicine_request/delete-request.html', context)

@login_required(login_url='login')
def request_list_view(request):
    requests = Request.objects.all()
    q = request.GET.get('search') if request.GET.get('search') != None else ''
    requests = Request.objects.filter(
        Q(requester__first_name__icontains=q)|
        Q(requester__last_name__icontains=q)|
        Q(medicine__icontains=q)
    )
    if request.method == 'POST':
        condition = request.POST.get('condition')
        if condition == 'Fulfilled':
            requests = Request.objects.filter(
                date_fulfilled__isnull=False
            )
        elif condition == 'Unfulfilled':
             requests = Request.objects.filter(
                date_fulfilled__isnull=True
            )
        else:
            requests = Request.objects.all()
    paginator = Paginator(requests, 5)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
           
    context = {'requests':requests, 'items':items}
    return render(request, 'medicine_request/request-list.html', context)
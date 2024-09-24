from django.shortcuts import render, redirect
from patients.models import Patient
from medicine_request.models import Request
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PatientSerializer
from datetime import datetime
from django.db.models import Sum
from django.contrib import messages
import logging

logger = logging.getLogger('__name__')

@login_required(login_url='login')
def home(request):
    patients = Patient.objects.all()
    patient_count = patients.count()
    request_count = Request.objects.count()
    fulfilled_count = Request.objects.filter(
        date_fulfilled__isnull=False
    ).count()  
    unfulfilled_count = Request.objects.filter(
        date_fulfilled__isnull=True
    ).count()
    quantity = Request.objects.filter(date_fulfilled__isnull=False).aggregate(quantity=Sum('quantity'))['quantity']
    if quantity == None:
        quantity = 0
    context = {'patient_count' : patient_count, 'request_count': request_count, 'fulfilled_count': fulfilled_count, 'unfulfilled_count': unfulfilled_count, 'quantity':quantity, }
    return render(request, 'base/index.html', context)

@api_view(['GET'])
def all_patient_count(request):
    patient_count = Patient.objects.count()  
    data = {'patient_count': patient_count}  
    return Response(data)

@api_view(['GET'])
def monthly_patient_count(request):
    now = datetime.now()
    patient_count = Patient.objects.filter(added__month=now.month, added__year=now.year).count()  
    data = {'patient_count': patient_count}  
    return Response(data)

@api_view(['GET'])
def today_patient_count(request):
    now = datetime.now()
    patient_count = Patient.objects.filter(added__month=now.month, added__year=now.year, added__day=now.day).count()  
    data = {'patient_count': patient_count}  
    return Response(data)

@api_view(['GET'])
def all_request_count(request):
    request_count = Request.objects.count()
    fulfilled_count = Request.objects.filter(
        date_fulfilled__isnull=False
    ).count()  
    unfulfilled_count = Request.objects.filter(
        date_fulfilled__isnull=True
    ).count()  
    data = {'request_count': request_count, 'fulfilled_count': fulfilled_count, 'unfulfilled_count': unfulfilled_count }  
    return Response(data)

@api_view(['GET'])
def monthly_request_count(request):
    now = datetime.now()
    request_count = Request.objects.filter(date_requested__month=now.month, date_requested__year=now.year).count()
    fulfilled_count = Request.objects.filter(
        date_fulfilled__isnull=False,date_requested__month=now.month, date_requested__year=now.year
    ).count()  
    unfulfilled_count = Request.objects.filter(
        date_fulfilled__isnull=True,date_requested__month=now.month, date_requested__year=now.year
    ).count()  
    data = {'request_count': request_count, 'fulfilled_count': fulfilled_count, 'unfulfilled_count': unfulfilled_count }  
    return Response(data)

@api_view(['GET'])
def today_request_count(request):
    now = datetime.now()
    request_count = Request.objects.filter(date_requested__month=now.month, date_requested__year=now.year, date_requested__day=now.day).count()
    fulfilled_count = Request.objects.filter(
        date_fulfilled__isnull=False,date_requested__month=now.month, date_requested__year=now.year, date_requested__day=now.day
    ).count()  
    unfulfilled_count = Request.objects.filter(
        date_fulfilled__isnull=True,date_requested__month=now.month, date_requested__year=now.year, date_requested__day=now.day
    ).count()  
    data = {'request_count': request_count, 'fulfilled_count': fulfilled_count, 'unfulfilled_count': unfulfilled_count }  
    return Response(data)

@api_view(['GET'])
def all_medicine_count(request):
    quantity = Request.objects.filter(
        date_fulfilled__isnull=False
    ).aggregate(quantity=Sum('quantity'))['quantity']
    data = {'quantity':quantity}
    return Response(data)

@api_view(['GET'])
def monthly_medicine_count(request):
    now = datetime.now()
    quantity = Request.objects.filter(date_requested__month=now.month, date_requested__year=now.year, date_fulfilled__isnull=False).aggregate(quantity=Sum('quantity'))['quantity']
    data = {'quantity':quantity}
    return Response(data)

@api_view(['GET'])
def today_medicine_count(request):
    now = datetime.now()
    quantity = Request.objects.filter(date_requested__month=now.month, date_requested__year=now.year, date_requested__day=now.day, date_fulfilled__isnull=False).aggregate(quantity=Sum('quantity'))['quantity']
    data = {'quantity':quantity}
    return Response(data)

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

@login_required(login_url='login')
def generate_report(request):
    patients = Patient.objects.all()
    requests = Request.objects.all()
    patient_count = patients.count()
    request_count = Request.objects.count()
    fulfilled_count = Request.objects.filter(
        date_fulfilled__isnull=False
    ).count()  
    unfulfilled_count = Request.objects.filter(
        date_fulfilled__isnull=True
    ).count()
    quantity = Request.objects.filter(
        date_fulfilled__isnull=False
    ).aggregate(quantity=Sum('quantity'))['quantity']
    data = {'patients': patients, 'requests': requests, 'patient_count' : patient_count, 'request_count': request_count, 'fulfilled_count': fulfilled_count, 'unfulfilled_count': unfulfilled_count, 'quantity':quantity,}
    html_string = get_template('base/report.html')
    html = html_string.render(data)
    
    # Create a HTTP response with PDF content
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="report.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    
    return response

@login_required(login_url='login')
def patient_report(request, pk):
    try:
        patient = Patient.objects.get(id=int(pk))
    except Exception as e:
        logger.error(f"{str(e)}")
        messages.error(request, "No patient found.")
        return redirect('patient-list')
    
    try:
        requests = Request.objects.filter(
            requester = patient
        )
    except Exception as e:
        logger.error(f"{str(e)}")
        messages.error(request, "Failed to fetch data.")
        return redirect('patient-list')
    
    patient_data = {
        'unfulfilled': 0,
        'fulfilled': 0,
        'fulfilled_med': 0,
        'unfulfilled_med': 0,
        'request_count' : requests.count() or 0,
        'checkups' : 0
    }

    if requests:
        for item in requests:
            if item.date_fulfilled:
                patient_data['fulfilled'] = patient_data['fulfilled'] + 1
                patient_data['fulfilled_med'] = patient_data['fulfilled_med'] + item.quantity
            else:
                patient_data['unfulfilled'] = patient_data['unfulfilled'] + 1
                patient_data['unfulfilled_med'] = patient_data['unfulfilled_med'] + item.quantity
            if item.check_up:
                patient_data['checkups'] = patient_data['checkups'] + 1
    
    context = {
        'patient_data' : patient_data,
        'requests' : requests,
        'patient' : patient
    }

    html_string = get_template('base/patient_report.html')
    html = html_string.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="patient_report.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    
    return response



def landing(request):
    return render(request, 'base/landing.html')


def error404(request):
    return render(request, '404.html')

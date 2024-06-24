from django.shortcuts import render
from patients.models import Patient
from medicine_request.models import Request
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PatientSerializer
from datetime import datetime
from django.db.models import Sum
from django.contrib import messages

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

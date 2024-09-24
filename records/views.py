from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Q

from .serializers import RecordSerializer, PatientSerializer
from .models import Records
from patients.models import Patient



# Create your views here.
@login_required(login_url='login')
def check_up_home(request):
    q = request.GET.get('search') if request.GET.get('search') != None else ''
    
    context = {}
    try:
        if q:
            records = Records.objects.filter(
                Q(patient__first_name__icontains=q)|Q(patient__last_name__icontains=q)|Q(checkup_details__icontains=q)|Q(date_added__icontains=q)
            )
        
        else:
            records = Records.objects.all()
    except:
        messages.error(request, "Failed to fetch necessary data. Please reload page.")
    
    paginator = Paginator(records, 10)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    
    context.update({
        'items' : items
    })

    return render(request, 'records/checkup.html', context)

@login_required(login_url='login')
def post_update_checkup(request, pk):
    try:
        record = Records.objects.get(id=int(pk))
    except:
        messages.error(request, "Patient does not exist.")
    
    if request.method.lower() == 'post':
        if record:
            record.checkup_details = request.POST.get('checkup')
            record.save()
            messages.success(request, 'Successfully updated checkup details')
            return redirect('check_up_home')

    context = {'record':record}
    return render(request, 'records/edit_checkup.html', context)

@login_required(login_url='login')
def post_create_checkup(request):
    try:
        patients = Patient.objects.all()
    except:
        messages.error(request, "Problem fetching data. Please try again.")
        return redirect('check_up_home')
    
    patient_data = []
    if patients:
        for patient in patients:
            data = PatientSerializer(patient)
            patient_data.append({data.data})
    
    if request.method.lower() == 'post':
        try:
            patient = Patient.objects.get(id=int(request.POST.get('patient_id')))
        except:
            messages.error(request, "Patient does not exist")
            return redirect('check_up_home')
        
        try:
            Records.objects.create(
                patient = patient,
                checkup_details = request.POST.get('checkup_details')
            )
        except:
            messages.error(request, "Failed to create new check up. Please try again.")
            return redirect('check_up_home')
        
        messages.success(request, "Successfully created new checkup")
        return redirect('check_up_home')
    


        

        

        



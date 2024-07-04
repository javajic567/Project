from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import Patient_form
from.models import Patient
# Create your views here.
def appointment(request):
    if request.method=='POST':
        form=Patient_form(request.POST)
        if form.is_valid():
            patient_name = request.POST.get('patient_name')
            patient_age = request.POST.get('patient_age')
            patient_email = request.POST.get('patient_email')
            appointment_cause = request.POST.get('appointment_cause')
            appointment_date=request.POST.get('appointment_data')
            doctor=request.POST.get('id')
            z=Patient(patient_name=patient_name,patient_age=patient_age,patient_email=patient_email,appointment_cause=appointment_cause,appointment_date=appointment_date,doctor=doctor)
            z.save()

        else:
            return HttpResponse('data not added')
    else:
        form=Patient_form()
        return render(request,'appointment.html',{'form':form})
def display(request):
    z=request.POST.get('patient_name')
    l='{} your appointment booked'.format(z)
    return render(request,'display.html',{'l':l})
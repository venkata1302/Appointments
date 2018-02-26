from django.shortcuts import render, HttpResponseRedirect,HttpResponse
from .models import Appointment
import datetime
import json



def home(request):
    return render(request,'home.html')

def search(request):
    if request.method == 'POST':
        if request.is_ajax():
            search_data = request.POST.get('search_data')
            query_set = Appointment.objects.filter(description__contains=search_data).order_by('date_time')
            data = [{'date':'{} {}'.format(str(item.date_time.strftime("%B")),str(item.date_time.strftime("%e"))),'time':'{}{}{} {}'.format(str(item.date_time.strftime("%I")),(':'),str(item.date_time.strftime("%M")),(str(item.date_time.strftime("%p"))).lower()),'description':item.description} for item in query_set]
            return HttpResponse(json.dumps(data),content_type = 'application/json')

def add_appointment(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        datetime_str = '{} {}'.format(date,time)
        datetime_obj = datetime.datetime.strptime(datetime_str,'%Y-%m-%d %H:%M')
        appointment1 = Appointment()
        appointment1.date_time = datetime_obj
        appointment1.description = request.POST.get('desc')
        appointment1.save()
    return HttpResponseRedirect('/home/')


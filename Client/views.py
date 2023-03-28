from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.template import loader
from django.urls import reverse
from .models import ClientInfo,RealTimeBill, BillingInfo, Billing
from django.views import generic
from .forms import NewUserForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
import datetime
from decimal import Decimal
import json



@login_required(login_url='/accounts/login/')  
def index(request):
    
    if request.user.is_authenticated:    
        dashboardinfo = RealTimeBill.objects.all().values()
        template = loader.get_template('client/dashboard.html')
        context = {
            'dashboardinfo' : dashboardinfo
        }
       
    else:
         template = loader.get_template('accounts/login.html')
    return HttpResponse(template.render({},request)) 


    
def signup(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save( )
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "errors")
	form = NewUserForm()
	return render (request=request, template_name="registration/signup.html", context={"register_form":form})

def dashboard(request):
    dashboardinfo = RealTimeBill.objects.all().values()
    template = loader.get_template('client/dashboard.html')
    context = {
        'dashboardinfo' : dashboardinfo
    }
    return HttpResponse(template.render({},request)) 


def savemeter(request):
    try:
        id = request.GET.get('meterid')
        
        client = ClientInfo.objects.get(meterid = id)
        
        if client:

            realtimeRecord = RealTimeBill.objects.filter(meterid_id = client.id, timestamp = datetime.date.today()).first()
            updateId = None
            msg = 'new record added'
            if realtimeRecord:
               updateId= realtimeRecord.id
               msg = 'update ID:' + str(updateId)
            
            total  = Decimal(request.GET.get('total'))
            current  = Decimal(request.GET.get('current'))
            newMeter = RealTimeBill(id = updateId ,meterid_id = client.id, totalconsumption = total, timestamp = datetime.date.today(), currentread = current)
            newMeter.switch = client.switch    
            addBillRecord(client.billingdate, newMeter)              
        
        newMeter.save()
        return JsonResponse({'switch': str(client.switch), 'msg':msg})
    except Exception as e:
        return JsonResponse({'error': e.args})
    
def addBillRecord(billdate, realtime):


    if (billdate.day+ 1 == realtime.timestamp.day): 
        realtimeRecord = RealTimeBill.objects.filter(meterid_id = realtime.meterid_id, timestamp = realtime.timestamp- datetime.timedelta(days = 1)).first()
       
        year = realtime.timestamp.year - 1 if realtime.timestamp.month == 1 else realtime.timestamp.year 
        month = 12 if realtime.timestamp.month == 1 else realtime.timestamp.month -1
        listing = Billing.objects.filter(meterid_id = realtime.meterid_id, billingyear = year, billingmonth = month).first()
        
        if listing is None:           
            billinfo = Billing(meterid_id = realtime.meterid_id, totalconsumed = realtime.totalconsumption, billingyear = year, billingmonth = month)
            listing = billinfo
            
        listing.totalconsumed = realtimeRecord.totalconsumption    
        listing.save()

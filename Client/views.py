import calendar
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
from .tool.functools import setLastMonth,setLastYear



@login_required(login_url='/accounts/login/')  
def index(request):
    
    if request.user.is_authenticated:
        template = loader.get_template('client/dashboard.html') 
        current_user = request.user 
        client = ClientInfo.objects.filter(user_id = current_user.id).first()
        if client != None:
            year = setLastYear(datetime.date.today().year, datetime.date.today().month)
            month = setLastMonth(datetime.date.today().month)
            billing = Billing.objects.filter(meterid_id = client.id, billingyear = year, billingmonth = month).first()
            if billing is None:
                billing = Billing.objects.filter(meterid_id = client.id, billingyear = year, billingmonth = month-1).first()
            realtime = RealTimeBill.objects.filter(meterid_id = client.id, timestamp = datetime.date.today()).first()
            
        period =   calendar.month_name[billing.billingmonth] +' '+ str(client.billingday) + ',' + str(year) + " - " + calendar.month_name[billing.billingmonth +  1] +' '+  str(client.billingday) + ',' + str(year) 

        context = {
            'client' : client,  
            'billing': billing,
            'realtime': realtime,
            'user': current_user,
            'period':period,
            'readdate': calendar.month_name[billing.billingmonth] +' '+ str(client.billingday) + ',' + str(year),
            'prevtotal': billing.totalconsumed * Decimal(1.90)
        }
       
    else:
         template = loader.get_template('accounts/login.html')
    return HttpResponse(template.render(context,request)) 


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
    current_user = request
    template = loader.get_template('client/dashboard.html')
    client = ClientInfo.objects.filter(user_id = id).first()
    if client != None:
        billing = Billing.objects.filter(meterid_id = client.meterid).first()
   
    context = {
        'client' : client,  
        'billing': billing,
        'user': current_user
    }
    return HttpResponse(template.render(context, request))


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
       
        year = setLastYear(realtime.timestamp.yearrealtime.timestamp.month)
        month = setLastYear(realtime.timestamp.month)
        listing = Billing.objects.filter(meterid_id = realtime.meterid_id, billingyear = year, billingmonth = month).first()
        
        if listing is None:           
            billinfo = Billing(meterid_id = realtime.meterid_id, totalconsumed = realtime.totalconsumption, billingyear = year, billingmonth = month)
            listing = billinfo
            
        listing.totalconsumed = realtimeRecord.totalconsumption    
        listing.save()
        
#@login_required(login_url='/accounts/login/')  
def settings(request,id):
    if request.user.is_authenticated:
        template = loader.get_template('client/updatesettings.html')
        client = ClientInfo.objects.filter(id=id).first()
        context = {'setting' : client}
    
    else:
        template = loader.get_template('accounts/login.html')
    return HttpResponse(template.render(context,request))


def updatesettings(request,id):
        checked = request.POST.get('switch-meter', False)
        template = loader.get_template('client/dashboard.html')
        client = ClientInfo.objects.filter(id = id).first()
        client.switch = checked
        client.save()
        context={}
        return HttpResponse(template.render(context,request))   
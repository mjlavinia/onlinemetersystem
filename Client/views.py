from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.template import loader
from django.urls import reverse
from .models import ClientInfo,RealTimeBill, BillingInfo
from django.views import generic
from .forms import NewUserForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from datetime import datetime
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
        test = RealTimeBill.objects.all().values()
        client = RealTimeBill.objects.get(meterid = id)
        total  = Decimal(request.GET.get('total'))
        current  = Decimal(request.GET.get('current'))
        newMeter = RealTimeBill(meterid = id, totalconsumption = total, timestamp = datetime.now(), currentread = current)
        newMeter.switch = True
        if client:
            newMeter.switch = client.switch
        newMeter.save()
        return JsonResponse({'switch': str(client.switch)})
    except Exception as e:
        return JsonResponse({'error': e.args[0]})


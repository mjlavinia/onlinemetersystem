from datetime import datetime, timedelta, date
from apscheduler.schedulers.background import BackgroundScheduler
from models import  BillingInfo, RealTimeBill, ClientInfo, Billing
from django.db.models import Sum
from django.db.models import DateTimeField, ExpressionWrapper, F


def schedule_api():
    todays = datetime.datetime(datetime.today().month, 4, datetime.today().year)
    
    
    dueClients = ClientInfo.objects.annotate(my_dt=ExpressionWrapper(F('billingdate__month') + F('billingdate__day'), output_field=DateTimeField()))

    dueClients = ClientInfo.objects.filter((billingdate__month) =datetime.now()-timedelta(days=1))

    for item in dueClients:
        consumed = RealTimeBill.objects.filter(timestamp__gte= item.billingstart, timestamp__lte = item.billingend, meterid = item.meterid).aggregate(Sum('totalconsumption'))
        billinfo = Billing()
            
            
        
            
            
            

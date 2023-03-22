from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
import datetime
# Create your models here.


class ClientInfo(models.Model):
    user = models.OneToOneField (User, null=True, on_delete=models.CASCADE)
    meterid = models.BigIntegerField()
    lastname = models.TextField(null=False, blank=False)
    firstname = models.TextField(null=False, blank=False)
    middleinitial = models.TextField(null=True, blank=False)
    address = models.TextField(null=False, blank=False)
    meterserial = models.TextField(null=False, blank=False)
    zone = models.TextField(null=True)
    billingdate=  models.DateField(blank = False)
    billingday = models.SmallIntegerField(null= False)
   
    
class BillingInfo(models.Model):
    meterid = models.BigIntegerField()
    previousreading = models.DecimalField(max_digits=10,decimal_places=2)
    presentreading = models.DecimalField(max_digits=10,decimal_places=2)
    currentwaterbill = models.DecimalField(max_digits=10,decimal_places=2)
    discount = models.DecimalField(max_digits=10,decimal_places=2)
    billingperiod = models.TextField(blank = False, default='')
    client_billinginfo = models.ForeignKey(ClientInfo, null=True ,on_delete=models.CASCADE)
   
    
class RealTimeBill(models.Model):
    meterid = models.BigIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True,null=True)
    totalconsumption = models.DecimalField(max_digits=8, decimal_places=4)
    currentread = models.DecimalField(max_digits=8, decimal_places=4)
    switch = models.BooleanField()
  #  client_billinginfo = models.ForeignKey(ClientInfo, null=True, on_delete=models.CASCADE)
    
    
class Billing(models.Model):
    meterid = models.BigIntegerField()
    totalconsumed =  models.DecimalField(max_digits=4, decimal_places=4)
    billingyear = models.IntegerField()
    
    



    

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
import datetime
# Create your models here.


class ClientInfo(models.Model):
    user = models.OneToOneField (User, null=True, on_delete=models.CASCADE)
    acoountnumber = models.CharField(null=False, blank=False, max_length=20, default='0000-0000-0000')
    meterid = models.BigIntegerField(editable=True, default=100000001, null=False, unique=True)
    lastname = models.CharField(null=False, blank=False, max_length=50)
    firstname = models.CharField(null=False, blank=False, max_length=50)
    middleinitial = models.CharField(null=True, blank=False, max_length=1)
    address = models.TextField(null=False, blank=False)
    meterserial = models.CharField(null=False, blank=False, max_length=12)
    zone = models.CharField(null=True,max_length=10)
    billingdate=  models.DateField(blank = True)
    billingday = models.SmallIntegerField(null= False)
    switch = models.BooleanField()
    
    def __str__(self):
        return str(self.meterid)
    
      
class BillingInfo(models.Model):
    meterid = models.ForeignKey(ClientInfo, default=1, verbose_name="MeterID", on_delete=models.SET_DEFAULT)
    previousreading = models.DecimalField(max_digits=18,decimal_places=2)
    presentreading = models.DecimalField(max_digits=18,decimal_places=2)
    currentwaterbill = models.DecimalField(max_digits=18,decimal_places=2)
    discount = models.DecimalField(max_digits=18,decimal_places=2)
    billingperiod = models.CharField(blank = False, default='', max_length=20)
   # client_billinginfo = models.ForeignKey(ClientInfo, null=True ,on_delete=models.CASCADE)
    
   
    
class RealTimeBill(models.Model):
    meterid = models.ForeignKey(ClientInfo, default=1, verbose_name="MeterID", on_delete=models.SET_DEFAULT)
    timestamp = models.DateField(auto_now_add=True,null=True)
    totalconsumption = models.DecimalField(max_digits=18, decimal_places=4)
    currentread = models.DecimalField(max_digits=18, decimal_places=4)
    
    class Meta:
        unique_together = ('meterid', 'timestamp',)

  #  client_billinginfo = models.ForeignKey(ClientInfo, null=True, on_delete=models.CASCADE)
    
    
class Billing(models.Model):
    meterid = models.ForeignKey(ClientInfo, default=1, verbose_name="MeterID", on_delete=models.SET_DEFAULT)
    totalconsumed =  models.DecimalField(max_digits=18, decimal_places=4)
    billingyear = models.IntegerField()    
    billingymonth = models.IntegerField()    
    
    
class Pricing(models.Model):
    rate = models.DecimalField(max_digits=18, decimal_places=4)
    discountpercent = models.DecimalField(max_digits=8,decimal_places=4)
    



    

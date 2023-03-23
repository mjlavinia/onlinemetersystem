from django.contrib import admin
from .models import BillingInfo,ClientInfo,RealTimeBill,Billing

admin.site.register(BillingInfo)
#admin.site.register(RealTimeBill)

admin.site.register(Billing)
# Register your models here..re

@admin.register(RealTimeBill)
class RealTimeBillAdmin(admin.ModelAdmin):
    list_display = ('meterid','totalconsumption','currentread')
 
 
@admin.register(ClientInfo)  
class CLientInforAdmin(admin.ModelAdmin):
    list_display = ('user','meterid','fullname')
    
    @admin.display(description='Name')
    def fullname(self,obj):
        return ("%s %s" % (obj.firstname, obj.lastname)).upper()
from django.contrib import admin
from django.forms import Select
from .models import BillingInfo,ClientInfo,RealTimeBill,Billing,MeterLog
from django_admin_inline_paginator.admin import TabularInlinePaginated

#admin.site.register(BillingInfo)
#admin.site.register(RealTimeBill)

admin.site.register(Billing)

class tabularRealtime(TabularInlinePaginated):
    model = RealTimeBill
    fields = ('timestamp', 'totalconsumption', 'currentread') 
    per_page = 10
    
class Billings(TabularInlinePaginated):
    model = Billing
    fields = ('billingmonth', 'billingyear', 'totalconsumed') 
    per_page = 10
    
    

@admin.register(ClientInfo)  
class CLientInforAdminWithPage(admin.ModelAdmin):
    list_display = ('meterid','fullname','switch','meterserial')
    inlines = (Billings,tabularRealtime)
    model = ClientInfo
    
    @admin.display(description='Name')
    def fullname(self,obj):
        return ("%s %s" % (obj.firstname, obj.lastname)).upper()

# Register your models here..re

@admin.register(RealTimeBill)
class RealTimeBillAdmin(admin.ModelAdmin):
    model = RealTimeBill
    list_display = ('timestamp', 'totalconsumption', 'currentread') 
    list_filter = ['meterid']

#class RealTimeBill(admin.TabularInline):
#    model = RealTimeBill
#    max_num = 10
#    min_num = 10
#    can_delete = False  
#    extra = 0
#    date_hierarchy = ('timestamp') 
#
#
#    def formfield_for_foreignkey(self, db_field, request, **kwargs):
#       if db_field.name == "timestamp":
#           kwargs["queryset"] =RealTimeBill.objects.all()
#           kwargs["widget"] = Select(attrs={"style": "width:400px"},)
#       return super().formfield_for_foreignkey(db_field, request, **kwargs)
# 
# 
#@admin.register(ClientInfo)  
#class CLientInforAdmin(admin.ModelAdmin):
#    list_display = ('meterid','fullname','switch','meterserial')
#    search_fields = ['lastname','meterid']
#    inlines = [
#        RealTimeBill
#    ]
#    @admin.display(description='Name')
#    def fullname(self,obj):
#        return ("%s %s" % (obj.firstname, obj.lastname)).upper()
    


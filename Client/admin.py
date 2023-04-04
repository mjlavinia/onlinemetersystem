from django.contrib import admin
from django.forms import Select
from .models import BillingInfo,ClientInfo,RealTimeBill,Billing

#admin.site.register(BillingInfo)
#admin.site.register(RealTimeBill)

admin.site.register(Billing)
# Register your models here..re

@admin.register(RealTimeBill)
class RealTimeBillAdmin(admin.ModelAdmin):
    list_display = ('meterid','totalconsumption','currentread')
    date_hierarchy = ('timestamp')

class RealTimeBill(admin.TabularInline):
    model = RealTimeBill
    max_num = 10
    min_num = 10
    can_delete = False  
    extra = 0
    date_hierarchy = ('timestamp') 


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
       if db_field.name == "timestamp":
           kwargs["queryset"] =RealTimeBill.objects.all()
           kwargs["widget"] = Select(attrs={"style": "width:400px"},)
       return super().formfield_for_foreignkey(db_field, request, **kwargs)
 
 
@admin.register(ClientInfo)  
class CLientInforAdmin(admin.ModelAdmin):
    list_display = ('meterid','fullname','switch','meterserial')
    search_fields = ['lastname','meterid']
    inlines = [
        RealTimeBill
    ]
    @admin.display(description='Name')
    def fullname(self,obj):
        return ("%s %s" % (obj.firstname, obj.lastname)).upper()
    



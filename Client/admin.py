from django.contrib import admin
from .models import BillingInfo,ClientInfo,RealTimeBill,Billing

admin.site.register(BillingInfo)
admin.site.register(RealTimeBill)
admin.site.register(ClientInfo)
admin.site.register(Billing)
# Register your models here..re

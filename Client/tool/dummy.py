import datetime
from django.http import HttpRequest, JsonResponse
from ..models import RealTimeBill,ClientInfo
from ..views import addBillRecord
def savefakemeter(request):
    try:
        import calendar, random

        year = int(request.GET.get('year'))
        month = int(request.GET.get('month'))
        id = int(request.GET.get('id'))
        num_days = calendar.monthrange(year, month)[1]
        client = ClientInfo.objects.filter(meterid = id).first()
        
        dates = []
        total = 0
        for day in range(1, num_days):
            number = random.randint(1, 20)
            date_str = f"{year}-{month:02d}-{day:02d}"
            dateData = datetime.date(year,month,day)
            
            total += number
            newMeter = RealTimeBill.objects.filter(meterid_id = client.id, timestamp = dateData).first()
            if newMeter == None:
                newdata = RealTimeBill( meterid_id= client.id, totalconsumption = total, timestamp = dateData, currentread =number)
                newMeter = newdata
            else:
                newMeter.totalconsumption = total
                newMeter.currentread = number
            newMeter.save()
            addBillRecord(client.billingdate, newMeter)
    
    except Exception as e:
            return JsonResponse({'error': e.args})
    
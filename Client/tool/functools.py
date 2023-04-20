import datetime
from django.utils import timezone

def setLastYear(year, month):
    yr =year - 1 if month == 1 else year 
    return yr
    
def setLastMonth(month):
   mo = 12 if month == 1 else month -1
   return mo


from datetime import datetime
def setTimeNotifications(date):
    sent_time = date
    current_time = timezone.now()
    time_since_sent = current_time - sent_time
    days_since_sent = time_since_sent.days
    hours_since_sent = int(time_since_sent.seconds / 3600)
    minutes_since_sent = int((time_since_sent.seconds % 3600) / 60)

    if days_since_sent > 0:
        message = f'{days_since_sent} days'
    elif hours_since_sent > 0:
        message = f'{hours_since_sent} hours'
    else:
        message = f'{minutes_since_sent} minutes ago.'

    return message


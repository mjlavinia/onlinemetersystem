import datetime

def setLastYear(year, month):
    yr =year - 1 if month == 1 else year 
    return yr
    
def setLastMonth(month):
   mo = 12 if month == 1 else month -1
   return mo
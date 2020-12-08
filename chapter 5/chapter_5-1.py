import time
import math
#chapter 5 ex 1 incomplete

 # epoch is equal to: 1 January 1970

 #date and time calculations

years_since_epoch= time.time()/(365.2422*24*60*60)
current_year=int(years_since_epoch)+1970
current_month=((years_since_epoch-int(years_since_epoch))*364.2422/30)+1
current_day=((current_month)-int(current_month))*29
current_hour=(current_day-int(current_day))*24
current_minute=(current_hour-int(current_hour))*60
current_second=(current_minute-int(current_minute))*60
current_month=int(current_month)
current_day=int(current_day)
current_hour=int(current_hour)
current_minute=int(current_minute)
current_second=int(current_second)
print('date:',current_year,'/',current_month,'/',current_day)
print('time:',current_hour,':',current_minute,':',current_second)

#current_month=(time.time()-(current_year*365.2422*24*60*60))/
                     
print(years_since_epoch, time.time())
print(time.gmtime(0)) 
"""
if (int(x)%4)==0 and  :
    


print(time.time(),'   ',x,'   ',time.gmtime(0))
"""
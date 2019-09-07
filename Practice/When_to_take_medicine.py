# ---------------------------------------------------PROBLEM STATEMENT------------------------------------------------------------------
#  
#  
# You visit a doctor on a date given in the format yyyy:mm:dd. Your doctor suggests you to take pills every alternate day 
# starting from that day. You being a forgetful person are pretty sure won’t be able to remember the last day you took the medicine 
# and would end up in taking the medicines on wrong days. So you come up with the idea of taking medicine on the dates whose day 
# is odd or even depending on whether dd is odd or even. Calculate the number of pills you took on right time before messing 
# up for the first time.
# 
# Note:
# Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100; 
# the centurial years that are exactly divisible by 400 are still leap years. For example, the year 1900 is not a leap year; 
# the year 2000 is a leap year.

def get_day(month):
    if month==1:return 31
    elif month == 2 : 
        if year%4==0: return 29 
        else: return 28
    elif month == 3 : return 31
    elif month == 4 : return 30
    elif month == 5 : return 31
    elif month == 6 : return 30
    elif month == 7 : return 31
    elif month == 8 : return 31
    elif month == 9 : return 30
    elif month == 10 : return 31
    elif month == 11 : return 30
    elif month == 12 : return 31

t = int(input("Number of test cases : "))

while t>=1:
    
    date = input("Enter in format yyyy:mm:dd  : ")
    date = date.split(":")
    year = int(date[0])
    month = int(date[1])
    day_of_med = int(date[2])
    no_of_days=0
    med_count=0
    
    while True:
        till_day = get_day(month)
        cur_day=0
        for i in range(day_of_med,till_day+1,2):
            cur_day=i
            med_count+=1
        
        if day_of_med%2==0:
            day_of_med=2
            if month!=12:
                month+=1
            else:
                month=1
            
            if(2+(till_day-cur_day)==2):
                pass
            else:
                break;
        else:
            day_of_med=1
            if month!=12:
                month+=1
            else:
                month=1
            
            if(1+(till_day-cur_day)==2):
                pass
            else:
                break;
            
    print(med_count)
    t-=1       
    
    
    
    
    
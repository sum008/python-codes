import time
from datetime import datetime as dt
from test.test_decimal import file

host_temp = "hosts"
host_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"
ip = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com","www.gmail.com","gmail.com"]
time_from = "10:00:00"
time_to = "19:00:00"

print( 10>1)
while True:
    
    cur_time = dt.now()
    print(cur_time)
    if (dt(dt.now().year,dt.now().month,dt.now().day,10,0,1) <=  dt.now() <=dt(dt.now().year,dt.now().month,dt.now().day,23 , 0,1)):
       
        with open(host_path,"r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write('\n')
                    file.write(ip+"   "+website)
    else:
        with open(host_path,"r+") as file:
            content = file.readlines() #puts pointer at the last line of file so the new line could be entered from there and not at the starting of file
            file.seek(0)  #puts pointer at the starting of file
            for line in content:
                if not any (website in line for website in website_list):
                    file.write(line)
            
            file.truncate()
                    
    time.sleep(3)

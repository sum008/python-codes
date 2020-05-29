import time
from datetime import datetime as dt

host_temp = "hosts"
host_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"
ip = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com","www.gmail.com","gmail.com"]


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
            content = file.readlines() f file
            file.seek(0)  
            for line in content:
                if not any (website in line for website in website_list):
                    file.write(line)
            
            file.truncate()
                    
    time.sleep(3)

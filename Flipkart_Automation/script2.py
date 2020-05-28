'''
Created on Apr 19, 2020

@author: Sumit
'''

from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.chrome.options import Options

import time
from robot.utils.error import Throwable

path_of_elements_per_page="//a[@class='_31qSD5']"
next_page_path1="//a[@class='_3fVaIS']"
next_page_path2="//a[@class='_3fVaIS'][2]"
search_bar_path="//input[@class='LM6RPg'][@title='Search for products, brands and more']"
serach_button_path="//button[@class='vh79eN'][@type='submit']"
price_path="//div[@class='_1vC4OE _2rQ-NK']"
rating_path="//div[@class='hGSR34']"
discount_path="//div[@class='VGWI6T']"

# _2AkmmA _29YdH8

def format_data(data):
    index=0
    for i in range(len(data)-1,0,-1):
        index+=1
        if data[i]==">":
            break
    data=data[len(data)-index+1:len(data)]
    
    return data

def automate():
#     cur_element=""
#     items=[]
    item=input("Enter your item ")
    budget=int(input("Budget ? "))
    rating=int(input("Enter your minimum rating "))
    link="https://www.flipkart.com"
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--window-size=1920x1080") 
#     driver = webdriver.Chrome(options=chrome_options,executable_path="D:\chromedriver.exe")
    driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")
    driver.get(link)
#     
#     
#     page=1
    newWindow = driver.window_handles[0]
    driver.switch_to.window(newWindow)
    driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']").click()
    driver.find_element_by_xpath(search_bar_path).send_keys(item)
    driver.find_element_by_xpath(serach_button_path).click()
    
    
    e=[]
    count=0
    time.sleep(1)
    while len(e)<=0 and count<=20:
        count+=1
        try:
            e=driver.find_elements_by_xpath("//div[@class='DUFPUZ']")
        except:
            
            continue
    
    if len(e)>0:
        print(e[0].text)
        driver.close()
        return
    
    u=driver.current_url
    print(u)
    source=requests.get(u).text
    soup=BeautifulSoup(source,"html5lib")
    time.sleep(1)
    f=[]
    click_rating="//div[@class='_4IiNRh _2mtkou'][@title='"+str(rating)+"★ & above']"
    while len(f)==0 :
        try:
            f=driver.find_elements_by_xpath(click_rating)
        except:
            continue
    f[0].click()
#     lis=soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['_1uv9Cb'])

#     lis=soup.find("div",{"class":["_1UoZlX","_3liAhj"]})
    lis=soup.select('div[class="_1UoZlX"]')
    if len(lis)==0: #_3dqZjq
        lis=soup.select('div[class="_3liAhj"]')
    if len(lis)==0: #_3dqZjq
        lis=soup.select('a[class="_3dqZjq"]')
    lis2=[]
    print(len(lis))
    e1=[]
    count1=0
    for i in lis:
        
#         if "_38sUEc" in str(i):
#             review=i.select('span[class="_38sUEc"]')
#             print(review)
#         else:
#             print("NOT PRESENT")
#         and '"hGSR34"' in str(i)

        while len(e1)<=0 and count1<=20:
            count1+=1
            try:
                e1=driver.find_elements_by_xpath("//span[@class='_38sUEc']")
            except:
                continue
    
        if len(e1)>0:
            if '"VGWI6T"' in str(i) and '"_38sUEc"' in str(i):
                lis2.append(i)
        else:
            if '"VGWI6T"' in str(i):
                lis2.append(i)
        
    print(len(lis2))       
    data=[]
    for i in lis2:
#         Price formatting
#         p=str(i.select('[class="_1vC4OE _2rQ-NK"]'))
        p=str(i.find("div",{"class":"_1vC4OE"}))
        p=p[p.index("₹")+1:]
        p=p[0:p.index("<")]
        if "," in p:
            p1=""
            p=p.split(",")
            for j in p:
                p1+=j
            p=p1
            
            
        review=str(i.select('span[class="_38sUEc"]'))
        if "Reviews" in review:
#                 print(review)
            index=review.index("Reviews")
            r=index-2
#             print(review)
            for k in range(index-2,0,-1):
                if review[k]==">":
                    break
                else:
                    r-=1
            review=review[r+2:index-1]
            if "," in review:
                review=review.split(",")
                r=""
                for l in review:
                    r+=l
                review=r
        else:
#             print(review)
            index=review.index("(")
            index1=review.index(")")
            review=review[index+1:index1]
            if "," in review:
                review=review.split(",")
                r=""
                for l in review:
                    r+=l
                review=r
#             print(review)
 
        if int(p)<=budget and int(review)>=5:
            
    #         Ratings formatting
            rate=str(i.select('[class="hGSR34"]'))
            rate=rate[0:rate.index("img")-1]
            rate=format_data(rate)
    #         Discount formatting
            dis=str(i.select('[class="VGWI6T"]'))
            dis=dis[0:dis.index("%")]
            dis=format_data(dis)
    #         Links formatting
            lin=str(i)
            count=lin.index("href")+7
            for j in range(lin.index("href")+7,len(lin)):
                if lin[j]!='"':
                    count+=1
                elif lin[j]=='"':
                    break
            
            lin=lin[lin.index("href")+7:count]
            
            data.append([int(p),float(rate),int(review),int(dis),lin])
            
    driver.close()    
    return data


def show_reviews(data,index):
    
    index-=1
    d=data[index]
#     print(d)
    link=d[4]
    
    link="https://www.flipkart.com/"+link
#     print(link)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080") 
    driver = webdriver.Chrome(options=chrome_options,executable_path="D:\chromedriver.exe")
    driver.get(link)
    
    review_rating=int(input("Review rating "))
#     swINJg _3nrCtb
    e=[]
    count=0
    time.sleep(1)
    while len(e)<=0 and count<=20:
        count+=1
        try:
            e=driver.find_elements_by_xpath("//div[@class='swINJg _3nrCtb']")
        except:
            continue
    
    if len(e)>0:
        e[0].click()
        
        
        time.sleep(1)
        read_more=[]
        count=0
        while len(read_more)<=0 and count<=20: #and count<=20:
            count+=1
            try:
                read_more=driver.find_elements_by_xpath("//span[@class='_1EPkIx']")
            except:
                continue
        
        if len(read_more)>0:
            for r in read_more:
                r.click()
            try:
                read_more[len(read_more)-1].click()
            except:
                pass
        print(len(read_more))
        time.sleep(1)
    #         link=driver.current_url
    #         source=requests.get(link).text
    #         soup=BeautifulSoup(source,"html5lib")
    #         //div[@class='ooJZfD _2oZ8XT col-9-12']/div[@class='_3gijNv col-12-12'][2]/div[@class='_1PBCrt']/div[@class='col']/div[@class='col _390CkK _1gY8H-']/div[@class='row']/div[@class='hGSR34 E_uFuv']
        count=len(driver.find_elements_by_xpath("//div[@class='col _390CkK _1gY8H-']"))
        for i in range(2,count+2):
            rating=driver.find_element_by_xpath("//div[@class='ooJZfD _2oZ8XT col-9-12']/div[@class='_3gijNv col-12-12']["+str(i)+"]/div[@class='_1PBCrt']/div[@class='col']/div[@class='col _390CkK _1gY8H-']/div[@class='row']/div[@class='hGSR34 E_uFuv']").text
            print(rating)
            if int(rating)>=review_rating:
                review=driver.find_element_by_xpath("//div[@class='ooJZfD _2oZ8XT col-9-12']/div[@class='_3gijNv col-12-12']["+str(i)+"]/div[@class='_1PBCrt']/div[@class='col']/div[@class='col _390CkK _1gY8H-']/div[@class='row']/div[@class='qwjRop']//div[@class]").text
                title=driver.find_element_by_xpath("//div[@class='ooJZfD _2oZ8XT col-9-12']/div[@class='_3gijNv col-12-12']["+str(i)+"]/div[@class='_1PBCrt']/div[@class='col']/div[@class='col _390CkK _1gY8H-']/div[@class='row']/p[@class='_2xg6Ul']").text
                print("Rating : "+str(rating))
                print(title)
                print()
                print(review)
                print()
    else:
        count=0
        while len(e)<=0 and count<=20:
            count+=1
            try:
                e=driver.find_elements_by_xpath("//div[@class='swINJg _3cycCZ']")
            except:
                continue
            
        e[0].click() 
        
        time.sleep(1)
        read_more=[]
        count=0
        while len(read_more)<=0 and count<=20: #and count<=20:
            count+=1
            try:
                read_more=driver.find_elements_by_xpath("//span[@class='_2jRR3v']")
            except: 
                continue
        
        if len(read_more)>0:
            for r in read_more:
                r.click()
            try:
                read_more[len(read_more)-1].click()
            except:
                pass
        print(len(read_more))
        time.sleep(1) 
        
        count=len(driver.find_elements_by_xpath("//div[@class='col _390CkK _1gY8H- _2675cp']"))
        for i in range(2,count+2):
            rating=driver.find_element_by_xpath("//div[@class='ooJZfD _2oZ8XT col-9-12']/div[@class='_3gijNv col-12-12']["+str(i)+"]/div[@class='_1PBCrt _26FBOm']/div[@class='col']/div[@class='col _390CkK _1gY8H- _2675cp']/div[@class='row']/div[@class='qwjRop _2675cp']/div")
            print(rating)
#             if int(rating)>=review_rating:
#                 review=driver.find_element_by_xpath("//div[@class='ooJZfD _2oZ8XT col-9-12']/div[@class='_3gijNv col-12-12']["+str(i)+"]/div[@class='_1PBCrt']/div[@class='col']/div[@class='col _390CkK _1gY8H-']/div[@class='row']/div[@class='qwjRop']//div[@class]").text
#                 title=driver.find_element_by_xpath("//div[@class='ooJZfD _2oZ8XT col-9-12']/div[@class='_3gijNv col-12-12']["+str(i)+"]/div[@class='_1PBCrt']/div[@class='col']/div[@class='col _390CkK _1gY8H-']/div[@class='row']/p[@class='_2xg6Ul']").text
#                 print("Rating : "+str(rating))
#                 print(title)
#                 print()
#                 print(review)
#                 print()
        
#         path_rating_review="//div[@class='ooJZfD _2oZ8XT col-9-12']/div[@class='_3gijNv col-12-12'][10]/div[@class='_1PBCrt _26FBOm']/div[@class='col']/div[@class='col _390CkK _1gY8H- _2675cp']/div[@class='row']/div[@class='qwjRop _2675cp']/div"   
        
        
#         lis=soup.select('div[class="col _390CkK _1gY8H-"]')
#         lis2=[len(lis)]
#         rating_data=[]
#         count=0
#         for i in lis:
#             if '"hGSR34 E_uFuv"' in str(i):
#                 rate=str(i.select('div[class="hGSR34 E_uFuv"]'))
#                 rate=rate[0:rate.index("img")-1]
#                 rate=int(format_data(rate))
#                 if rate>=review_rating:
#                     print("Rating "+ str(rate))
#                     l=[]
#                     l.append(rate)
#                     if '"_2xg6Ul"' in str(i):
#                         title=str(i.select('p[class="_2xg6Ul"]'))
#                         title=title[0:len(title)-5]
#                         title=format_data(title)
#                         print(title)
#                     else:
#                         print("No title")
#                         
#                     if '"qwjRop"' in str(i):
#                         review=driver.find_element_by_xpath("//div[@class='ooJZfD _2oZ8XT col-9-12']/div[@class='_3gijNv col-12-12']["+str(count+2)+"]/div[@class='_1PBCrt']/div[@class='col']/div[@class='col _390CkK _1gY8H-']/div[@class='row']/div[@class='qwjRop']//div[@class]").text
# #                         review=str(i.select('div[class=""]'))
#                         print(review)
#                         print()
#                     else:
#                         print("No Review")
#                 count+=1
#                     lis2.append(i)
    while True:
        pass

    
    
    
#     lis=soup.select('div[class="col _390CkK"]')
#     lis2=[]
#     rating_data=[]
#     for i in lis:    
#         if "hGSR34 E_uFuv" in str(i):
#             rate=str(i.select('div[class="hGSR34 E_uFuv"]'))
#             rate=rate[0:rate.index("img")-1]
#             rate=int(format_data(rate))
#             if rate>=review_rating:
#                 lis2.append(i)
                
                
    
        
            
            
    

try:          
    data=automate()
except Throwable as t:
    print(t)
if data!=None: 
    count=1   
    for i in data:
        print(count,i)
        count+=1
        print()
        
index=int(input("Enter index "))
show_reviews(data, index)

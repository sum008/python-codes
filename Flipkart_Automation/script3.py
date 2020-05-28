'''
Created on Apr 24, 2020

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
    chrome_options = Options()
    chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--window-size=800x700") 
    driver = webdriver.Chrome(options=chrome_options,executable_path="D:\chromedriver.exe")
#     driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")
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
    
    time.sleep(1)
    lis=driver.find_elements_by_xpath("//div[@class='_1UoZlX']")
    if len(lis)==0: #_3dqZjq
        lis=driver.find_elements_by_xpath("//div[@class='_3liAhj']")
    if len(lis)==0: #_3dqZjq
        lis=driver.find_elements_by_xpath("//a[@class='_3dqZjq']")
    print(len(lis))   
    data=[] 
    review_list=[]
    starts=0
    price=0
    discount=0
    no_of_ratings=0
    no_of_reviews=0
    for i in lis:
        i.click()
        try:
            driver.switch_to.window(driver.window_handles[1])
        except:
            driver.switch_to.window(driver.window_handles[0])
            continue
                
        #-----------------PRICE--------------------------------
        price=str(driver.find_element_by_xpath("//div[@class='_1vC4OE _3qQ9m1']").text)
        if "," in price:
            p=""
            price=price.split(",")
            for j in price:
                p+=j
            price=int(p[1:])
        else:
            price=int(price[1:])
#         print("price ",price)
        
        #--------------------DISCOUNT-------------------------------------
        
        try:
            
            discount=str(driver.find_element_by_xpath("//div[contains(@class,'VGWI6T _1iCvwn')]").text)
            discount=int(discount[0:discount.index("%")])
        except:
            discount=0
            
        try:
            stars=0
            stars=driver.find_element_by_xpath("//div[contains(@class,'hGSR34')]").text
            stars=float(stars)
        except:
            pass
#         print(price,discount,stars)
        if price<=budget and discount>0 and stars>=rating:
#             print(price,discount)
            #--------------------NAME--------------------------------    
            name=driver.find_element_by_xpath("//span[@class='_35KyD6']").text
            
            #--------------------CURRENT URL------------------------------
            
            c_url=driver.current_url
    
    #         print("discount ",discount)
            #---------------------REVIEW AND RATING---------------------------
            try:
                no_of_ratings=0
                no_of_reviews=0
                d=str(driver.find_element_by_xpath("//span[@class='_38sUEc']/span[1]").text)
    #             print(d)
                d=d.split("&")
                no_of_ratings=d[0]
                no_of_reviews=d[1]
                
                no_of_ratings=no_of_ratings[0:no_of_ratings.index("R")-1]
                if "," in no_of_ratings:
                    p=""
                    no_of_ratings=no_of_ratings.split(",")
                    for j in no_of_ratings:
                        p+=j
                    no_of_ratings=int(p)
                else:
                    no_of_ratings=int(no_of_ratings)
                    
                no_of_reviews=no_of_reviews[0:no_of_reviews.index("R")-1]
                if "," in no_of_reviews:
                    p=""
                    no_of_reviews=no_of_reviews.split(",")
                    for j in no_of_reviews:
                        p+=j
                    no_of_reviews=int(p)
                else:
                    no_of_reviews=int(no_of_reviews)
            except:
                pass
            
            
            data.append([name,price,stars,discount,no_of_ratings,no_of_reviews,c_url])
            
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    print("DOne",len(data))
    return [data,review_list]   

def view_review(link):
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--window-size=800x700") 
    driver = webdriver.Chrome(options=chrome_options,executable_path="D:\chromedriver.exe")
#     driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")
    driver.get(link)
    
    time.sleep(1.5)
    
    try:
        driver.find_element_by_xpath("//div[contains(@class,'swINJg')]").click()
        print("sdfs")
    except:
        pass
    
    read_more=[]
    count=0
    while len(read_more)<=0 and count<=20: #and count<=20:
        count+=1
        try:
            read_more=driver.find_elements_by_xpath("//*[text()='READ MORE']")
        except:
            continue
    
    if len(read_more)>0:
        for r in read_more:
            try:
                r.click()
            except:
                pass
        try:
            read_more[len(read_more)-1].click()
        except:
            pass
    time.sleep(1)    
    t=driver.find_elements_by_xpath("//div[contains(@class,'390CkK')]")
    for k in t:
        print(k.text)
        

try:          
    data=automate()
    review=data[1]
    data=data[0]
except Throwable as t:
    print(t)
if data!=None:  
    for i in range(0,len(data)):
        print(i+1,data[i])
        print()
        
        
        
index=int(input("Enter index"))
view_review(data[index-1][6])
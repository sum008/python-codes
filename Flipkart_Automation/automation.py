from selenium import webdriver
import time

path_of_elements_per_page="//a[@class='_31qSD5']"
next_page_path1="//a[@class='_3fVaIS']"
next_page_path2="//a[@class='_3fVaIS'][2]"
link="https://www.flipkart.com"
search_bar_path="//input[@class='LM6RPg'][@title='Search for products, brands and more']"
serach_button_path="//button[@class='vh79eN'][@type='submit']"
price_path="//div[@class='_1vC4OE _2rQ-NK']"
rating_path="//div[@class='hGSR34']"
discount_path="//div[@class='VGWI6T']"

# _2AkmmA _29YdH8

def format_(price):
    price=str(price[1:])
    price=price.split(",")
    price=price[0]+price[1]
    price=int(price)
    return price

def automate():
    cur_element=""
    items=[]
    item=input("Enter your item ")
    print("Enter your budget min and max budget")
    budget_min,budget_max=map(int,(input()))
    rating=int(input("Enter your minimum rating "))
    
    click_rating="//div[@class='_4IiNRh _2mtkou'][@title='"+str(rating)+"★ & above']"
    click_discount="//div[@class='_4IiNRh _2mtkou'][@title='10% or more']"
  
    driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")
    driver.get(link)
    page=1
    newWindow = driver.window_handles[0]
    driver.switch_to.window(newWindow)
    driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']").click()
    driver.find_element_by_xpath(search_bar_path).send_keys(item)
    driver.find_element_by_xpath(serach_button_path).click()
    time.sleep(1)
    f=[]
    while len(f)==0 :
        try:
            f=driver.find_elements_by_xpath(click_rating)
        except:
            continue
    f[0].click()
    time.sleep(1)
    e=[]
    while len(e)<=0:
        try:
            e=driver.find_elements_by_xpath("//*[@id='container']/div/div[3]/div[2]/div[1]/div[1]/div/div[1]/div/section[16]/div/div")
        except:
            continue
    e[0].click()
    time.sleep(1)
    d=[]
    while len(d)<=0 :
        try:
            d=driver.find_elements_by_xpath(click_discount)
        except:
            continue
    d[0].click()
    time.sleep(1)
    while page<=10:
        cur_element=[]
        cur_price=[]
        cur_discount=[]
        cur_rating=[]
        while len(cur_element)<=0:
                try:
                    cur_element=driver.find_elements_by_xpath(path_of_elements_per_page)
                    cur_price=driver.find_elements_by_xpath(price_path)
                    cur_discount=driver.find_elements_by_xpath(discount_path)
                    cur_rating=driver.find_elements_by_xpath(rating_path)
                except:
                    continue
#         print(len(cur_price),len(cur_rating),len(cur_discount))
        for i in range(0,24):
#             print(i)
            
            price=cur_price[i].text
            price=format_(price)
            cur_price[i]=price
#             print(price,i)
            rate=cur_rating[i].text
            rate=float(rate)
            cur_rating[i]=rate
            
            disc=cur_discount[i].text
            disc=str(disc)
            disc=int(disc[0:disc.index("%")])
            cur_discount[i]=disc
            
            if price<=budget_max and price>=budget_min and rate>=rating:
#                 print(cur_price[i],cur_rating[i],cur_discount[i])
                href=cur_element[i].get_attribute("href")
                items.append([href,cur_price[i],cur_rating[i],cur_discount[i]])
                
        if page==1:
            driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[26]/div/div/nav/a[11]/span").click()
        else:
            driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[26]/div/div/nav/a[12]/span").click()
        print(page)
        page+=1
        time.sleep(2)

    print(items,len(items))
            
automate()
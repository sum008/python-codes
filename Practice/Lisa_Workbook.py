def workbook(n, k, arr):
#     k is total number of questions per page
#       n is number of chapters
#       arr denotes number of questions in each chapter

    page_no=1 
    count=0
    count1=0
    for i in range(1,n+1):
        
        for j in range(1,arr[i-1]+1):
           
            count1+=1
            
            if page_no==j:
                count+=1
                
            if count1==k:
                page_no+=1
                count1=0
                         
        if count1!=0:
            page_no+=1
            count1=0
            
    return count
    
    
arr =[4,2,6,1,10]

print(workbook(5, 3, arr))



# x=0
# sum=0
# n=90
# for i in range(15,n,15):
#     if i%15==0:
#         x+=i   
#         
# print(x)
# sum_three =  ((2*3+(((n-1)//3)-1)*3)*((n-1)//3))//2     
# sum_five =   ((2*5+(((n-1)//5)-1)*5)*((n-1)//5))//2
# sum=sum_three+sum_five
# print((sum-x))  
# print(n//15)
# print(n%15)
            
            
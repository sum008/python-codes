def func_check(a):
    
    count=1
    temp=a[0]
    
    for i in range(1,len(a)):
        if temp==a[i]:
            count+=1
            print(count,i,a[i])
        else:
            temp=a[i]
            count=1
            
        if count==7:
            return "danger" 
    if count<7:
        return "safe"
  
  
a = "011001000000011"

print(func_check(a))          
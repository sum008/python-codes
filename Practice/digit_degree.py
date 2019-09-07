
def func_check(n):
    count=0
    n=str(n)
    if len(n)==1:
        return 0
    else:
        while not len(n)==1:
            a=0
            count+=1
            for i in n:
                a=a+int(i)    
            n=str(a) 
        return count  
    
    
print(func_check(999999999999999999999999999)) 
def func_binary(n):

    rem=""
    result=""
    
    while not n==0:
        
        rem=rem+str(n%2)
        n=int(n/2)
    
    for i in rem[len(rem)::-1]:
        result=result+i
        
    return result

print(func_binary(11))


def func_chk(n):
    result=0
    count=0
    a="101"
    pos=0
    for i in n:
        if count<3 and i == a[pos%3]:
            count+=1
            pos+=1
            if count==3:
                result+=1
                
        elif count==3:
            pos=1
            if i==a[pos%3]:
                count=2
                pos+=1
            else:
                count=0
                pos=0
            
        else:
            pos=0
            count=0
            
    return result

print(func_chk("001010100101"))
    
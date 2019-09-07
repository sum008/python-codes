import math
  
def solve(n):
    s = str(n)
    sum1=0
    sum2=0
    for i in s:
        sum1=sum1+int(i)
         
    s=""
     
    while n%2==0:
        s=s+str(2)
        n=int(n/2)
         
    for i in range(3, int(math.sqrt(n))+1,2):
         
        while n%i==0:
            s=s+str(i)
            n=int(n/i)
     
    if n!=1:
        s=s+str(n)
         
    for i in s:
        sum2=sum2+int(i)
       
    if sum1==sum2:
        return 1
     
    return 0
     
print(solve(100))



# def summingSeries(n):
#     sum1 = (((n%1000000007)*(n%1000000007))%1000000007)
#     return sum1
# 
# print(summingSeries(229137999))    
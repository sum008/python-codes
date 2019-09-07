a = open("C:\\Users\\Sumit\\Desktop\\input15.txt","r")
con = a.read()
b=list(con.split(" "))
c=[]
for i in b:
    c.append(int(i))

c.sort(reverse=False)
print(c)
count=0
n=99878
max_=0
prev=0
count1=0
count2=0
for i in range(0,n):
        
    for j in c:
        if count==0:
            x=abs(i-j)
            count=1
            prev=x   
        else:
            x = abs(i-j)
            if prev<x:
                count1+=1
                x=prev
                break
            else:
                count2+=1
                prev=x
   
    count=0
    
    if x>max_:
        max_= x

print( max_ , count1,count2)
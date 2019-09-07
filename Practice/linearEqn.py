
n=int(input("Enter no. of unknowns"))
a=[]
if n==1:
    for i in range(1,4):
        x=int(input())
        a.append(x)
    
    print((a[2]-a[1])/a[0])
elif n==2:
    for i in range(1,7):
        x=int(input("Enter equation"))
        a.append(x)
    if a[0]!=a[3]:
        b=a
        print(len(a),len(b))
        for i in range(0,3):
            a[i]=a[i]*b[3]
        print(a)    
        for i in range(3,6):
            a[i]=a[i]*b[0]
        print(a)    
        y=(a[2]-a[5])/(a[1]-a[4])
        x=(b[2]-b[1]*y)/b[0]
        print(x,y)
        
    elif a[0]==a[3]:
        y=(a[2]-a[5])/(a[1]-a[4])
        x=(b[2]-b[1]*y)/b[0]
        print(x,y)
    
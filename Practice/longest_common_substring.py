x = "zxabcdezy"
y = "yzabcdezx"

max_=0
count=0
pos=0
longest=""
final_longest=""
for i in range(0,len(y)):
    
    while pos<len(x):
        if y[i]==x[pos]:
            count+=1
            pos+=1
            longest+=y[i]
            break
        if count>max_:
            max_=count
            final_longest=longest
#             print(max_,longest)
            count=0
        else:
            count=0
            longest=""
            pos+=1
    if pos==len(x) or i==len(y)-1:
        if count>max_:
            max_=count
            final_longest=longest
#             print(max_,longest)
        count=0
        longest=""
        pos=0
         
print(max_,final_longest)        
        

import time

def longestCommonSubsequence(a, b):
    x=a
    y=b
    pos_stk_x=[]
    posx=0
    posy=0
    count=0
    longest=""
    final_long=""
    max_=0
    c=0
    tempy=0
    while True:
        
        if c==0:
            pos_stk_x.append(posx)
        print(posx,posy," yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
        
        if  posx<len(x) and x[posx]==y[posy]:
            print(x[posx],y[posy],"lololllllllllllololollllll")
            count+=1
            longest+=x[posx]
            posx+=1
            posy+=1
            tempy=posy
            c=1
            if posy==len(y):
                if max_<count:
                    max_=count
                    final_long=longest
#                 print(final_long,max_," ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")
                count=0
                longest=""
                posx=pos_stk_x.pop()+1
                if posx>=len(x):
                    break
#                 print(posx,"  posssssssssssssssssssssssssssssssssssssssssposssssssssssssssssssssssssssssssssssssss")
                tempy=posy
                posy=0
                c=0
            
        elif posy<=len(y)-1 and posx<len(x):
            
            while tempy<len(y) and x[posx]!=y[tempy]:
                if tempy<len(y):
                    tempy+=1
                else:
                    break
            c=1
            if tempy<len(y) and x[posx]==y[tempy]:
                print(x[posx],y[tempy],"iiiiiiiiiiiiiiiiiiiiiiiiii")
                posy=tempy
            else:
                tempy=posy
                posx+=1
            
        elif posy>=len(y) or posx>=len(x)-1:
            if max_<count:
                max_=count
                final_long=longest
#             print(final_long,max_," ddddddddddddddddd")
            count=0
            longest=""
            posx=pos_stk_x.pop()+1
            if posx>=len(x):
                return final_long
            
            print(posx,"  posssssssssssssssssssssssssssssssssssssssssposssssssssssssssssssssssssssssssssssssss")
            tempy=posy
            posy=0
            c=0



x="abcbdab"        
y="bdcaba"

print(longestCommonSubsequence(x, y))
    
    
    
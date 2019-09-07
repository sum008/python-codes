def equalStacks(h1, h2, h3):   
    h1.reverse(),h2.reverse(),h3.reverse()
    count1=sum(h1)
    count2=sum(h2)
    count3=sum(h3)
    while not count1==count2==count3:
        if count1>count2 or count1>count3:
            while not count1 <= count2 and len(h1)!=0:
                x=h1.pop()
                count1=count1-x
                
            while not count1 <= count3 and len(h1)!=0:
                x=h1.pop()
                count1=count1-x
                
        if count2>count1 or count2>count3:
            while not count2 <= count1 and len(h2)!=0:
                x=h2.pop()
                count2=count2-x
                
            while not count2 <= count3 and len(h2)!=0:
                x=h2.pop()
                count2=count2-x
                
        if count3>count1 or count3>count2:
            while not count3 <= count1 and len(h3)!=0:
                x=h3.pop()
                count3=count3-x
                
            while not count3 <= count2 and len(h3)!=0:
                x=h3.pop()
                count3=count3-x
                
        if len(h1)==0 or len(h2)==0 or len(h3)==0:
            return 0
    return count1

              
h1=[3 ,2 ,1 ,1 ,1]
h2 = [4,3,2]
h3=[1,1,4,1]
 
print(equalStacks(h1, h2, h3))
                    
                
                
                
                
                
                
                
                
                
                
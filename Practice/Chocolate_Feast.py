# 10 2 5
# 12 4 4
# 6 2 2

def chocolateFeast(n, c, m):
    
    total_chocolate = n//c 
    wrapper_current=total_chocolate 
      
    while True:
        print("x")
        if wrapper_current>=m:
            
            if m-wrapper_current == 0:
                total_chocolate+=1
                break
              
            total_chocolate += (wrapper_current//m )
            wrapper_current = (wrapper_current//m ) + (wrapper_current%m )
        if wrapper_current<=0:
            break
        
        if wrapper_current <m:
            break
        
    return total_chocolate
    
    
print(chocolateFeast(6 ,2 ,2))
            
            
        
        
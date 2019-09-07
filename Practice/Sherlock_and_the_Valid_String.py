def isValid(s):
    
    valid_str={}
    valid_str2=[]
    count=1
    
    for i in s:
        if not i in valid_str:
            valid_str.update({i:count})
        else:
            valid_str.update({i:valid_str[i]+1})
    
    for i in valid_str.values():
        valid_str2.append(i)
                
    valid_str2.sort(reverse=True)
    print(valid_str2)
    prev=valid_str2[0]
    count=0
    diff=0
    for i in range(1,len(valid_str2)):
        if prev != valid_str2[i]:
            count+=1
            
    print(count)
    
    if count>1:
        return False
    else:
        for i in range(1,len(valid_str2)):
            if valid_str2[i-1] != valid_str2[i]:
                if valid_str2[i]>1:
                    return False
                elif valid_str2[i] ==1:
                    return True
                diff=valid_str2[i-1]-valid_str2[i]
                print(diff)
        
        if diff>1:
            return False
        else:
            return True 
    
print(isValid("abcdefghhgfedecba"))
            
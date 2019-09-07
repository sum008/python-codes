def arrayManipulation(n,queries):
    
    res = [0]*n
    count=0
    max_val=0
    while count!=len(queries)-1:
        sum = queries[count][2]
        start_index = queries[count][0]-1
        end_index = queries[count][1]
        
        for i in range(start_index,end_index):
            res[i]=res[i]+sum
            if res[i]>max_val:
                max_val=res[i]
                
        count+=1
                
    return max_val
    
arrayManipulation(10)
    
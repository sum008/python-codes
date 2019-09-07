
def func_check(bi ,bj, pi,pj):
    
    #for diagonal up right
    while 0<=bi<=7 and 0<=bj<=7:
        bi=bi-1
        bj=bj+1
        if bi==pi and bj==pj:
            return True
    
    #for diagonal up left
    while 0<=bi<=7 and 0<=bj<=7:
        bi=bi-1
        bj=bj-1
        if bi==pi and bj==pj:
            return True
        
    #for diagonal down left
    while 0<=bi<=7 and 0<=bj<=7:
        bi=bi+1
        bj=bj-1
        if bi==pi and bj==pj:
            return True
        
    #for diagonal down right
    while 0<=bi<=7 and 0<=bj<=7:
        bi=bi+1
        bj=bj+1
        if bi==pi and bj==pj:
            return True
        
    return False

bishop_x=8
bishop_y=8
pawn_x=6
pawn_y=8

print(func_check(bishop_x-1,bishop_y-1,pawn_x-1,pawn_y-1))
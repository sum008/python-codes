print("# 7=00  #8=01  #9=02")
print("# 4=10  #5=11  #6=12")
print("# 1=20  #2=21  #3=22")

player1 = input ( "Enter player1 name : " )
player2 = input ( "Enter player2 name : " )

dic = {player1 : "x" , player2 : "0"}
lis = [ player1 , player2 ]
row = 3
column = 3
mat = [ [ "*" , "*" , "*" ] ,
        [ "*" , "*" , "*" ] ,
        [ "*" , "*" , "*" ] ]


def play() :
    t = 0
    while True :
        mov = str ( input ( "Enter your position {} : ".format ( lis [ t % 2 ] ) ) )
        if mov == "7" :
            if mat [ 0 ] [ 0 ] == "*" :
                mat [ 0 ] [ 0 ] = dic [ lis [ t % 2 ] ]
                print_the_matrix ( mat )
                check_for_x_0 ( 0 , 0 , mat , dic [ lis [ t % 2 ] ] , lis [ t % 2 ] )
                check_for_tie ( mat )
            else :
                print ( "Invalid position" )
                t = t - 1

        elif mov == "8" :
            if mat [ 0 ] [ 1 ] == "*" :
                mat [ 0 ] [ 1 ] = dic [ lis [ t % 2 ] ]
                print_the_matrix ( mat )
                check_for_x_0 ( 0 , 1 , mat , dic [ lis [ t % 2 ] ] , lis [ t % 2 ] )
                check_for_tie ( mat )
            else :
                print ( "Invalid position" )
                t = t - 1
        elif mov == "9" :
            if mat [ 0 ] [ 2 ] == "*" :
                mat [ 0 ] [ 2 ] = dic [ lis [ t % 2 ] ]
                print_the_matrix ( mat )
                check_for_x_0 ( 0 , 2 , mat , dic [ lis [ t % 2 ] ] , lis [ t % 2 ] )
                check_for_tie ( mat )
            else :
                print ( "Invalid position" )
                t = t - 1
        elif mov == "4" :
            if mat [ 1 ] [ 0 ] == "*" :
                mat [ 1 ] [ 0 ] = dic [ lis [ t % 2 ] ]
                print_the_matrix ( mat )
                check_for_x_0 ( 1 , 0 , mat , dic [ lis [ t % 2 ] ] , lis [ t % 2 ] )
                check_for_tie ( mat )
            else :
                print ( "Invalid position" )
                t = t - 1

        elif mov == "5" :
            if mat [ 1 ] [ 1 ] == "*" :
                mat [ 1 ] [ 1 ] = dic [ lis [ t % 2 ] ]
                print_the_matrix ( mat )
                check_for_x_0 ( 1 , 1 , mat , dic [ lis [ t % 2 ] ] , lis [ t % 2 ] )
                check_for_tie ( mat )
            else :
                print ( "Invalid position" )
                t = t - 1

        elif mov == "6" :
            if mat [ 1 ] [ 2 ] == "*" :
                mat [ 1 ] [ 2 ] = dic [ lis [ t % 2 ] ]
                print_the_matrix ( mat )
                check_for_x_0 ( 1 , 2 , mat , dic [ lis [ t % 2 ] ] , lis [ t % 2 ] )
                check_for_tie ( mat )
            else :
                print ( "Invalid position" )
                t = t - 1

        elif mov == "1" :
            if mat [ 2 ] [ 0 ] == "*" :
                mat [ 2 ] [ 0 ] = dic [ lis [ t % 2 ] ]
                print_the_matrix ( mat )
                check_for_x_0 ( 2 , 0 , mat , dic [ lis [ t % 2 ] ] , lis [ t % 2 ] )
                check_for_tie ( mat )
            else :
                print ( "Invalid position" )
                t = t - 1

        elif mov == "2" :
            if mat [ 2 ] [ 1 ] == "*" :
                mat [ 2 ] [ 1 ] = dic [ lis [ t % 2 ] ]
                print_the_matrix ( mat )
                check_for_x_0 ( 2 , 1 , mat , dic [ lis [ t % 2 ] ] , lis [ t % 2 ] )
                check_for_tie ( mat )
            else :
                print ( "Invalid position" )
                t = t - 1

        elif mov == "3" :
            if mat [ 2 ] [ 2 ] == "*" :
                mat [ 2 ] [ 2 ] = dic [ lis [ t % 2 ] ]
                print_the_matrix ( mat )
                check_for_x_0 ( 2 , 2 , mat , dic [ lis [ t % 2 ] ] , lis [ t % 2 ] )
                check_for_tie ( mat )
            else :
                print ( "Invalid position" )
                t = t - 1
        t = t + 1


def print_the_matrix(mat) :
    for i in range ( 0 , row ) :
        for j in range ( 0 , column ) :
            print ( mat [ i ] [ j ] ,end = " | " )
        print ( )


def check_for_x_0(a , b , mat , move , name) :
    count = 0
    c=a #a=position row
    # left
    for j in range ( b - 1 , -1 , -1 ) :
        if j >= 0 and mat [ a ] [ j ] == move :
            count = count + 1

        else :
            if count > 0 :
                count = count - 1
            
            break
    # rigth
    if count <= 1 :
        for j in range ( b + 1 , column ) :
            if j <= column - 1 and mat [ a ] [ j ] == move :
                count = count + 1

            else :
                if count > 0 :
                    count = count - 1
                
                break

    # up
    if count <= 1 :
        for i in range ( a - 1 , -1 , -1 ) :
            if i >= 0 and mat [ i ] [ b ] == move :
                count = count + 1

            else :
                if count > 0 :
                    count = count - 1
                break

    # down
    if count <= 1 :
        for i in range ( a + 1 , row ) :
            if i <= row - 1 and mat [ i ] [ b ] == move :
                count = count + 1
                print("down")
            else :
                if count > 0 :
                    count = count - 1
                break

    # diagonal up left
    if count <= 1 :
        for j in range ( b - 1 , -1 , -1 ) :
            c = c - 1
            if c >= 0 and j >= 0 and mat [ c ] [ j ] == move :
                count = count + 1
                print("up left")
            else :
                if count > 0 :
                    count = count - 1
                break
    c=a
    # diagonal down right
    if count <= 1 :
        for j in range ( b + 1 , column ) :
            c = c + 1
            if c <= row - 1 and j <= column - 1 and mat [ c ] [ j ] == move :
                count = count + 1
            else :
                if count > 0 :
                    count = count - 1
                break
    c=a
    # diagonal up right
    if count <= 1 :

        for j in range ( b + 1 , column ) :
            c = c - 1
            if c >= 0 and j <= column and mat [ c ] [ j ] == move :
                count = count + 1
            else :
                if count > 0 :
                    count = count - 1
                break
    c=a
    # diagonal down left
    if count <= 1 :
        for j in range ( b - 1 , -1 , -1 ) :
            c = c + 1
            if c <= row - 1 and j >= 0 and mat [ c ] [ j ] == move :
                count = count + 1

            else :
                if count > 0 :
                    count = count - 1
                break

    if count == 2 :
        print ( "You won {}".format ( name ) )
        exit ( 0 )


def check_for_tie(mat) :
    chk = 0
    for i in range ( 0 , row ) :
        for j in range ( 0 , column ) :
            if mat [ i ] [ j ] == "*" :
                chk = 1
                break
            elif i == row - 1 and j == column - 1 :
                print ( "Its a tie" )
                exit ( 0 )

        if chk == 1 :
            break

play ( )

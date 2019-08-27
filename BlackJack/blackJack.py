import random
x=22/7
print(x)
suit = ("hearts" , "diamonds" , "spades" , "clubs")
value = ("two" , "three" , "four" , "five" , "six" , "seven" , "eight" , "nine" , "ten" , "jack" , "queen" , "king" , "ace")
val = {"two" : 2 , "three" : 3 , "four" : 4 , "five" : 5 , "six" : 6 , "seven" : 7 , "eight" : 8 , "nine" : 9 ,
       "ten" : 10 , "jack" : 10 , "queen" : 10 , "king" : 10 , "ace" : 11}
cards = [ ]



class Card ( ) :
    suit = ""
    value = 0

    def __init__(self , suit , value) :
        self.suit = suit
        self.value = value

    def __str__(self) :
        return self.suit + " " + str ( self.value )


for i in suit :
    for j in value :
        cards.append ( Card ( i , val [ j ] ) )

def play_again():
    pl=input("Want to play again y/n? : ")
    if(pl=="y"):
        return True
    else:
        return False


def play_the_game(chp) :
    chip=chp
    print("You have {} chips ".format(chip))
    print()
    if chip==0:
        yn=input("You have no chip left, want to reset? y/n : ")
        if yn=="y":
            chip=100
        else:
            print("No? Do you want to play without chip? No chip No game ")
            print()
            exit(0)
    bet=int(input("How much do you want to bet? : "))
    while bet>chip:
        print("You don't have enough chip ")
        print()
        bet=int(input("How much do you want to bet? : "))

    player = cards.pop ( )
    print ( "Player card " + str ( player.suit ) )
    print()
    print ( "Card points " + str ( player.value ) )
    print()
    count_player = player.value
    player = cards.pop ( )
    print ( "Player card " + str ( player.suit ) )
    print()
    print ( "Card points " + str ( player.value ) )
    print("-------------------------------------------")
    count_player = count_player + player.value
    print ( "Player points " + str ( count_player ) )
    print("-------------------------------------------")
    computer = cards.pop ( )
    print ( "Computer card " + str ( computer.suit ) )
    print()
    print ( "Card value " + str ( computer.value ) )
    print("-------------------------------------------")
    count_comp = computer.value
    print ( "Computer points " + str ( count_comp ) )
    print("-------------------------------------------")
    play = True

    while play==True:
        count=0
        move=input("Enter your move : hit/stop : ")
        print()
        while move=="hit":
            player = cards.pop ( )
            count_player = count_player + player.value
            print ( "Player card " + str ( player.suit ) )
            print()
            print ( "Card points " + str ( player.value ) )
            print("-------------------------------------------")
            print ( "Player points " + str ( count_player ) )
            print("-------------------------------------------")
            if count_player==21:
                print("Player won")
                print()
                chip=chip+bet
                print("You have now {} chips ".format(chip))
                print()
                play=play_again()
                if play==False:
                    exit(0)
                else :
                    play_the_game(chip)
            elif count_player>21:
                print("Player lose")
                print()
                chip=chip-bet
                print("You have now {} chips ".format(chip))
                print()
                play=play_again()
                if play==False:
                    exit(0)
                else :
                    play_the_game(chip)

            move=input("Enter your move : hit/stop : ")
            print()

        if count>0:
            if count_player>count_comp:
                print("player won")
                print()
                chip=chip+bet
                print("You have now {} chips ".format(chip))
                print()
                play=play_again()
                if play==False:
                    exit(0)
                else :
                    play_the_game(chip)

        computer=cards.pop()
        print ( "Computer card " + str ( computer.suit ) )
        print()
        print ( "Card value " + str ( computer.value ) )
        print("-------------------------------------------")
        count_comp = count_comp+computer.value
        print ( "Computer points " + str ( count_comp ) )
        print("-------------------------------------------")
        count=count+1
        while count_comp<17:
            computer=cards.pop()
            print ( "Computer card " + str ( computer.suit ) )
            print()
            print ( "Card value " + str ( computer.value ) )
            print("-------------------------------------------")
            if computer.value==11:
                if count_comp+computer.value <=21:
                    count_comp = count_comp+computer.value
                else:
                    count_comp = count_comp+1
            else:
                count_comp = count_comp+computer.value

            print ( "Computer points " + str ( count_comp ) )
            print("-------------------------------------------")

        if count_comp==21:
            print("computer won")
            print()
            chip=chip-bet
            play=play_again()
            if play==False:
                exit(0)
            else :
                play_the_game(chip)
        elif count_comp>21:
            print("computer lose")
            print()
            chip=chip+bet
            print("You have now {} chips ".format(chip))
            print()
            play=play_again()
            if play==False:
                exit(0)
            else :
                play_the_game(chip)
        elif count_comp>count_player:
            print("computer won")
            print()
            chip=chip-bet
            print("You have now {} chips ".format(chip))
            print()
            play=play_again()
            if play==False:
                exit(0)
            else :
                play_the_game(chip)
        elif count_comp<count_player:
            print("Player won")
            print()
            chip=chip+bet
            print("You have now {} chips ".format(chip))
            print()
            play=play_again()
            if play==False:
                exit(0)
            else :
                play_the_game(chip)

        elif count_comp==count_player:
            print("It's a tie! You still have {} chips ".format(chip))
            print()
            play=play_again()
            if play==False:
                exit(0)
            else :
                play_the_game(chip)


class Implement():

    chip=100
    random.shuffle ( cards )
    play_the_game(chip)


t = Implement()

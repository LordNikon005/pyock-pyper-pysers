import os

#set defaults RPS for P1 and P2
rock1 = False
rock2 = False
paper1 = False
paper2 = False
scissors1 = False
scissors2 = False

print("Player 1,")
player_one_gate = input("(R)ock, (P)aper or (S)cissors?")

if player_one_gate == "R":
    rock1 = True

elif player_one_gate == "P":
    paper1 = True

elif player_one_gate == "S":
    scissors1 = True

os.system('cls')
print("Player 2,")
player_two_gate = input("(R)ock, (P)aper or (S)cissors?")

if player_two_gate == "R":
    rock2 = True

elif player_two_gate == "P":
    paper2 = True

elif player_two_gate == "S":
    scissors2 = True


#start workig out who tf wins

if player_one_gate == "R":
    if rock1 == rock2:
        os.system('cls')
        print("Rock VS Rock")
        print("Its a tie!")
        os.system('pause')
    elif rock1 == paper2:
        os.system('cls')
        print("Rock VS Paper")
        print("Player 2 Wins!")
        os.system('pause')
    elif rock1 == scissors2:
        os.system('cls')
        print("Rock VS Scissors")
        print("Player 1 Wins!")
        os.system('pause')

elif player_one_gate == "P":
    if paper1 == rock2:
        os.system('cls')
        print("Paper VS Rock")
        print("Player 1 Wins!")
        os.system('pause')
    elif paper1 == paper2:
        os.system('cls')
        print("Paper VS Paper")
        print("Its a tie!")
        os.system('pause')
    elif paper1 == scissors2:
        os.system('cls')
        print("Paper VS Scissors")
        print("Player 2 Wins!")
        os.system('pause')

elif player_one_gate == "S":
    if scissors1 == rock2:
        os.system('cls')
        print("Scissors VS Rock")
        print("Player 2 Wins!")
        os.system('pause')
    elif scissors1 == paper2:
        os.system('cls')
        print("Scissors VS Paper")
        print("Player 1 Wins!")
        os.system('pause')
    elif scissors1 == scissors2:
        os.system('cls')
        print("Scissors VS Scissors")
        print("It a Tie!")
        os.system('pause')
    
    
        
        
        

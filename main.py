#init
import random

#main
while True: 
    choices = ["rock", "paper", "scissors"]     
    compchoice = random.choice(choices)
    player = input("rock, paper or scissors?: ").lower()

    lost = "You Lose :( "
    won = "You Won!"

    if player == compchoice:
        print('Tie!')
    elif player == "rock":
        if compchoice == "scissors":
            print(won)
        else:
            print(lost)
    elif player == "paper":
        if compchoice == "rock":
            print(won)
        else:
            print (lost)
    elif player == "scissors":
        if compchoice == "paper":
            print(won)
        else:
            print(lost)

#print choices
    print("computer: " + compchoice)
    print("player: "+ player)
#determines whether the game continues
    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break
print("Bye!")



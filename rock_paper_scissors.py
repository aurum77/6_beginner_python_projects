from random import randint

print("Input 1 for Rock, 2 for Paper, 3 for Scissors")

player = int(input("Input a number: "))
computer = randint(1, 3)

while True:

    # You chose Rock, you beat Scissors
    if(player == 1 and computer == 3):
        print("You won!")
        break

    # You chose Paper, you beat Rock
    elif(player == 2 and computer == 1):
        print("You won!")
        break

    # You chose Scissors, you beat Paper
    elif(player == 3 and computer == 2):
        print("You won!")
        break
    
    # You chose the same object as the computer did
    elif(player == computer):
        print("Tie!")
        break

    else:
        print("You lose!")
        break

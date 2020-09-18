from random import randint

rand_num = randint(0, 20)

while True:
    guess = int(input("Enter a number between 0-20 = "))

    if(guess == rand_num):
        print("Congrats you have found the number")
        break

    elif(guess > rand_num):
        print("You must go lower")

    elif(guess < rand_num):
        print("You must go higher")
    
    else:
        print("Wrong Answer")

from random import randint

rand_num = randint(0, 20)

# debug
print(rand_num)
while True:
    guess = input("Enter a number between 0-20 = ")

    if(int(guess) == rand_num):
        print("Congrats you have found the number")
        break
    
    print("You have guessed it wrong, ")

    if(int(guess) > rand_num):
        print("You must go lower")

    if(int(guess) < rand_num):
        print("You must go higher")


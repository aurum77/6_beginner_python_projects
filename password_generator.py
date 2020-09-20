import random
import string

letters_num = 0
numbers_num = 0

while(letters_num + numbers_num < 6):

    letters_num = int(input("How many numbers do you want in your password ? "))
    numbers_num = int(input("How many letters/symbols do you want in your password ? "))
    
    if(letters_num + numbers_num < 6):
        print("The sum of letter and number count must be at least 6")

letters_cnt = 0
numbers_cnt = 0
passwd = []
# string.printable[0:10] can be used for the numbers
# string.printable[10:95] can be used for the characters and symbols 

while True:
    
    rand = random.randint(0,1)

    if(letters_cnt != letters_num and rand == 0):
        passwd.append(random.choice(string.printable[10:95]))
        letters_cnt += 1

    if(numbers_cnt != numbers_num and rand == 1):
        passwd.append(random.choice(string.printable[0:10]))
        numbers_cnt += 1

    if(letters_cnt == letters_num and numbers_cnt == numbers_num):
        break

print(''.join(passwd))

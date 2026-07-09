import random
num=input("Guess the number between 1 and 100: ")
secret_num = random.randint(1, 100)
while int(num) != secret_num:
    if int(num) < secret_num:
        print("Too low!")
    else:
        print("Too high!")
    num=input("Guess again: ")
print("Congratulations! You guessed the number.")
import random
name = input("Hello! What is your name?") # kbtu
a = random.randint(1,20)
cnt = 0
while True:
    if cnt == 0:
        b = int(input(f"Well, {name}, I am thinking of a number between 1 and 20. Take a guess."))
    else:
        b = int(input())
    if a > b:
        print("Your guess is too low. Take a guess.")
        cnt += 1
    elif a < b:
        print("Your guess is too high. Take a guess.")
        cnt += 1
    elif a == b:
        print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
        break
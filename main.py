import random

guessCount = 1
sercretNumber = random.randint(0, 100)
print("I am thinking of a number between 0 - 100")
while True:
    guess = float(input("What's your guess?"))
    if (guess == sercretNumber):
        break
    if (guess > sercretNumber):
        print("Your guess is too high!")
        guessCount = guessCount + 1 
    if (guess < sercretNumber):
        print("Your guess is too low!")
        guessCount = guessCount + 1 
print("Congrats! Your got it in", guessCount, "times!")
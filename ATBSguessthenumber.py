# Write your code here :-)
#GUESS THE NUMBER GAME#
import random, math
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

#Ask the player to guess 6 times#
for guessesTaken in range(1,7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Too low!')
    elif guess > secretNumber:
        print('Too high!')
    else:
        break #This condition is the correct guess!


if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope, the number i was thinking of was ' + str(secretNumber))

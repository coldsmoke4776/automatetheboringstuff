# Write your code here :-)
import random, math, sys, os

print('ROCK, PAPER.....SCISSORS!!!!')

#Variables to keep track of wins, losses and ties
wins = 0
losses = 0
ties = 0

#The main game loop
while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')#Player input loop
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break #break out of player input loop
        print('Make your move by typing either r,p,s or q to quit')

    #Display player choice
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    #Display computer choice
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    #Display and record wins/losses/ties
    if playerMove == computerMove:
        print('Its a tie! Boring....')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('Hell yeah, you won!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('Hell yeah, you won!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('Hell yeah, you won!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('Damn, you lost!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('Damn, you lost!')
        losses = losses +1
    elif playerMove == 's' and computerMove == 'r':
        print('Damn, you lost!')
        losses = losses + 1


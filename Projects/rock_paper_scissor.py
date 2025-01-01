"""
    Rock Paper Scissor.
    Created on June 10, 2023.
    Made by T0N1.
"""
import random
#           rock paper scissor
# rock      tie  lose  win
# paper     win  tie   lose
# scissor   lose win   tie
print('The rules of the game goes thus:\nRock vs Paper=> Paper wins\nPaper vs Scissor=> Scissor wins\nScissor vs '
      'Rock=> '
      'Rock wins')
print('\nYou have the options to pick [r]ock, [p]aper, or [s]cissor.')
user = input("Enter your choice: ")


def rps(human):
    results = {1: ['r', 'rock'], 2: ['p', 'paper'], 3: ['s', 'scissor']}
    computer = random.randint(1, 3)
    if human in ['r', 'rock']:
        num = 1
        if computer == num:
            print(f"Computer: {results[computer][1]}\nTie.")
        elif num < computer < len(results):
            print(f'Computer: {results[computer][1]}\nYou lose.')
        else:
            print(f'Computer: {results[computer][1]}\nYou win.')

    elif human in ['p', 'paper']:
        num = 2
        if computer == num:
            print(f"Computer: {results[computer][1]}\nTie.")
        elif computer < num:
            print(f'Computer: {results[computer][1]}\nYou win.')
        else:
            print(f'Computer: {results[computer][1]}\nYou lose.')

    elif human in ['s', 'scissor']:
        num = 3
        if computer == num:
            print(f"Computer: {results[computer][1]}\nTie.")
        elif 1 < computer < num:
            print(f'Computer: {results[computer][1]}\nYou win.')
        else:
            print(f'Computer: {results[computer][1]}\nYou lose.')
    else:
        print('Please enter a valid option!')


rps(user)

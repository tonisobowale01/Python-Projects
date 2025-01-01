"""
    Coin Tossing Simulator.
    Created on June 08, 2023.
    Made by T0N1.
"""
import random

print('Welcome, you have the option to enter [h]eads or [t]ails.')
coin_side_input = input('Enter input: ')


def coin_toss(user):
    results = {1: ['heads', 'h'], 2: ['tails', 't']}
    if user in {'h', 'heads', 't', 'tails'}:
        coin = random.randint(1, 2)
        if coin == 1:
            if user in results[coin]:
                print(f'The coin flipped: {results[coin][0]}\nYou win.')
            else:
                print(f'The coin flipped: {results[coin][0]}\nYou lose.')
        else:
            if user in results[coin]:
                print(f'The coin flipped: {results[coin][0]}\nYou win.')
            else:
                print(f'The coin flipped: {results[coin][0]}\nYou lose.')
    else:
        print('Please enter a valid option between [h]eads and [t]ails')


coin_toss(coin_side_input)

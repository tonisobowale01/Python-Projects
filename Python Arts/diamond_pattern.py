"""
    BroFar's Diamond Pattern Challenge.
    Created on February 11, 2023.
    Made by T0N1.
"""

for line in range(4):
    for two in range(15):
        if two == 0 or two == 14:
            print(' ' * 12 + 'o...o' + ' ' * 23 + 'o...o')
        elif two == 1 or two == 13:
            print(' ' * 12 + '.....' + ' ' * 23 + '.....')
        elif two == 2 or two == 12:
            print(' ' * 8 + 'o...o. .o...o' + ' ' * 15 + 'o...o. .o...o')
        elif two == 3 or two == 11:
            print(' ' * 8 + '..o..   ..o..' + ' ' * 15 + '..o..   ..o..')
        elif two == 4 or two == 10:
            print(' ' * 4 + 'o...o...     ...o...o' + ' ' * 7 + 'o...o...     ...o...o')
        elif two == 5 or two == 9:
            print(' ' * 4 + '..o....       ....o..       ..o....       ....o..')
        elif two == 6 or two == 8:
            print('o...o...o.         .o...o...o...o...o.         .o...o...o')
        elif two == 7:
            print('..o...o..           ..o...o...o...o..           ..o...o..')

"""
    BroFar's Diamond Box Challenge.
    Created on February 14, 2023.
    Made by T0N1.
"""
# 33 lines
# 24 up and down
# 9 inner
# open('.png', 'w').write('')
for line in range(33):
    if line == 0 or line == 32:
        print(' ' * 17 + '.')
    elif line == 1 or line == 31:
        print(' ' * 16 + '. .')
    elif line == 2 or line == 30:
        print(' ' * 15 + '.   .')
    elif line == 3 or line == 29:
        print(' ' * 14 + '.     .')
    elif line == 4 or line == 28:
        print(' ' * 13 + '.       .')
    elif line == 5 or line == 27:
        print(' ' * 12 + '.         .')
    elif line == 6 or line == 26:
        print(' ' * 11 + '.     .     .')
    elif line == 7 or line == 25:
        print(' ' * 10 + '.     . .     .')
    elif line == 8 or line == 24:
        print(' ' * 9 + '.     . . .     .')
    elif line == 9 or line == 23:
        print(' ' * 8 + '.     . . . .     .')
    elif line == 10 or line == 22:
        print(' ' * 7 + '.     . .   . .     .')
    elif line == 11 or line == 21:
        print(' ' * 6 + '.......................')
    elif line == 12:
        print(' ' * 5 + '.      /        \\      .')
    elif line == 13:
        print(' ' * 4 + '...    /    /\\    \\    ...')
    elif line == 14:
        print(' ' * 3 + '. ...  /    .  .    \\  ... .')
    elif line == 15:
        print(' ' * 2 + '. . . ./    ......    \\. . . .')
    elif line == 16:
        print(' ' * 1 + '. .   . .   ...  ...   . .   . .')
    elif line == 17:
        print(' ' * 2 + '. . . .     ......     . . . .')
    elif line == 18:
        print(' ' * 3 + '. ... \\     .  .    /  ... .')
    elif line == 19:
        print(' ' * 4 + '...   \\     \\/    /    ...')
    elif line == 20:
        print(' ' * 5 + '.     \\         /      .')
# print('''<style>img{display:none}body{font-size:70%;color:gold;}</style>''')

# unfinished
"""
    Three Ar row Head Challenge.
    Created on XXXX XX, 2023.
    Made by T0N1
"""
print('.'.center(75))
outer, inner = 36, 1
while inner < 14:
    if inner == 13:
        print(' ' * (outer - 5) + '.' + ' ' * (outer - 24) + '.' + ' ' * (inner-4) + '.' + ' ' * (outer - 24) + '.')
    else:
        print(' ' * outer + '.' + ' ' * inner + '.')
    outer -= 1
    inner += 2
new = 7
space = 20
old = 6
print(' ' * space + '.' + ' ' * new + '.' + ' ' * old + '. . . .' + ' ' * old + '.' + ' ' * new + '.')
while new < 27:

    new += 3
    space -= 1
    old -= 1

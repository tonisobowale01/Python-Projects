"""
    R🌺's Kite Pattern Challenge.
    Created on February 08, 2023.
    Made by T0N1.
"""
outside = 6
num = 1
outside1 = 1
num1 = 11
last1 = 1
for each in range(4):
    print(" " * outside + '*' * num)
    outside -= 2
    num += 4
for each in range(6):
    print(" " * outside1 + '*' * num1)
    outside1 += 1
    num1 -= 2
for last in range(3):
    print(' ' * (outside1 - 1) + '* ' * last1)
    outside1 -= 1
    last1 += 1

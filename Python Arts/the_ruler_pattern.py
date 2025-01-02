"""
    Emms's Ruler Pattern Challenge.
    Created on February 09, 2023.
    Made by T0N1.
"""
print(' _______ ')
print(f'|0      |')
number = 1
for i in range(16):
    if i in [4, 9, 14]:
        print(f'|---{number}px |')
        number += 1
    elif i == 15:
        print('|_______|')
    else:
        print('|-      |')

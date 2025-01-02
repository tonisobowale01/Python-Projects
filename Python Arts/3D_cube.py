"""
    Brofar's 3D Cube Challenge.
    Created on January 29, 2023.
    Made by T0N1.
"""

print(' ' * 33 + '...............')
outer = 12
inner = 0
space = 32
while inner < 6:
    print(' ' * space + '.' + ' ' * inner + '.' + ' ' * outer + '.' + ' ' * inner + '.')
    outer -= 1
    inner += 1
    space -= 1
print(' ' * 26 + '...............' + ' ' * 6 + '.')

for i in range(2):
    print(' ' * 26 + '.      .      .      .')
print(' ' * 26 + '.' + ' ' * 6 + '...............')

while inner > 0:
    print(' ' * 26 + '.' + ' ' * (inner - 1) + '.' + ' ' * (outer + 1) + '.' + ' ' * (inner - 1) + '.')
    outer += 1
    inner -= 1
    space += 1
print(' ' * 26 + '...............')

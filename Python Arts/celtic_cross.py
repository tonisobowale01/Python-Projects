"""
    This is my first approach to a console art challenge, I hope you love it.
    Created on January 29, 2023.
    Made by T0N1.
"""

print(' ' * 35 + '@@@@@')
print(' ' * 34 + '@ @ @ @')
print(' ' * 33 + '@ @ @ @ @')
print(' ' * 32 + '@@@ +++ @@@')
print(' ' * 34 + '@  @  @')
print(' ' * 34 + '@@   @@')
for i in range(7):
    if i == 0 or i == 6:
        print(' ' * 25 + '@@@@@' + ' ' * 6 + '@@@' + ' ' * 6 + '@@@@@')
    elif i == 1 or i == 5:
        print(' ' * 24 + '@@@  @' + ' ' * 7 + '@' + ' ' * 7 + '@  @@@')
    elif i == 2 or i == 4:
        print(' ' * 23 + '@@@@ + @' + ' ' * 6 + '@' + ' ' * 6 + '@ + @@@@')
    elif i == 3:
        print(' ' * 22 + '@@@ + @ @@@@@@<0>@@@@@@ @ + @@@')
print(' ' * 34 + '@@   @@')
print(' ' * 33 + '@   @   @')
print(' ' * 32 + '@@@ +++ @@@')
print(' ' * 33 + '@ @ @ @ @')
print(' ' * 34 + '@ @ @ @')
print(' ' * 35 + '@@@@@')
for i in range(2):
    print(' ' * 37 + '@')
print(' ' * 36 + '@@@')
print(' ' * 37 + '@')
end = 0
ash = '@@@@@'
space = 35
while end < 3:
    print(' ' * space + ash)
    end += 1
    space -= 1
    ash += '@@'
print(' ' * 31 + '@@@@@@@@@@@@@')

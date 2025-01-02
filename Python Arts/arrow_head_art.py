"""
    Created on January 30, 2023.
    Made by T0N1.
    Just for fun(●'◡'●)
"""

print('. . . . . . . . . . . . . . .\n'
      '. . . . . . . . . . . . . . .')
outer, inner = 11, 1
print('. .' + ' ' * outer + '.' + ' ' * outer + '. .')
outer -= 1
while inner < 21:
    if inner == 15:
        print('. .' + ' ' * (outer + 2) + '.' + ' ' * (inner-4) + '.' + ' ' * (outer + 2) + '. .')
    elif inner == 17:
        print('. .' + ' ' * (outer + 5) + '. . . . .' + ' ' * (outer + 5) + '. .')
    elif inner == 19:
        print('. . . . . . . . . . . . . . .\n'
              '. . . . . . . . . . . . . . .')
    else:
        print('. .' + ' ' * outer + '.' + ' ' * inner + '.' + ' ' * outer + '. .')
    outer -= 1
    inner += 2

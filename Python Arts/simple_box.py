"""
    BroFar's Simple Box Pattern Challenge.
    Created on February 09, 2023.
    Made by T0N1.
"""

outside = 22
inside = -4
print()
print()
for line in range(12):
    if line == 0:
        print(' ' * outside + 'UP')
    elif line == 1:
        print(' ' * outside + '/\\.\\********************\\.\\')
    elif line == 2:
        print(' ' * outside + '/..\\.\\********************\\.\\')
    else:
        print(' ' * outside + '/./' + ' ' * inside + '\\.\\********************\\.\\')
    outside -= 1
    inside += 2
print(' ' * (outside - 1) + '(========== ( ) ==========) ******************) .)')
for line in range(13, 25):
    if line == 22:
        print(' ' * (outside + 1) + '\\.\\../********************/./')
    elif line == 23:
        print(' ' * (outside + 1) + '\\.\\/********************/./')
    elif line == 24:
        print(' ' * (outside + 1) + 'DOWN')
    else:
        print(' ' * (outside + 1) + '\\.\\' + ' ' * (inside - 2) + '/./********************/./')
    outside += 1
    inside -= 2

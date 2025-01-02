noises = input()
noises = noises.split(' ')
animal = ""
for i in noises:
    if i == 'Grr':
        animal += 'Lion '
    elif i == 'Rawr':
        animal += 'Tigers '
    elif i == 'Ssss':
        animal += 'Snakes '
    else:
        animal += 'Birds '
print(animal)

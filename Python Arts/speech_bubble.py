<<<<<<< HEAD
"""
    Dronto's Speech Bubble Challenge.
    Created on February 10, 2023.
    Made by T0N1.
"""
# Please input a text that is 8 characters,
# if it is more than that it will break the pattern.
text = input()
print()
open('../../../../Documents/Codebook/Python Challenges/.png', 'w').write('')
for each in range(7):
    if each == 0 or each == 6:
        print(' ' * 6 + '*' * 15)
    elif each == 1 or each == 5:
        print(' ' * 4 + '**' + ' ' * 15 + '**')
    elif each == 2 or each == 4:
        print(' ' * 3 + '*' + ' ' * 19 + '*')
    # This, you can change the font-size to allow your text to fit in the speech bubble.
    # Next time I will find a way to make the text responsive to the bubble.
    else:
        print(' ' * 3 + '*' + ' ' * 7 + "<span style='font-size:10px;'>" + text + "</span>" + ' ' * 7 + '*')
number = 4
for last in range(4):
    if last == 3:
        print(' ' * 16 + '*' * number)
    else:
        print(' ' * 17 + '*' * number)
    number -= 1
print('''<style>
            img{display:none;}
            body{font-size:95%;}
        </style>''')
=======
"""
    Dronto's Speech Bubble Challenge.
    Created on February 10, 2023.
    Made by T0N1.
"""
# Please input a text that is 8 characters,
# if it is more than that it will break the pattern.
text = input()
print()
open('../../../../Documents/Codebook/Python Challenges/.png', 'w').write('')
for each in range(7):
    if each == 0 or each == 6:
        print(' ' * 6 + '*' * 15)
    elif each == 1 or each == 5:
        print(' ' * 4 + '**' + ' ' * 15 + '**')
    elif each == 2 or each == 4:
        print(' ' * 3 + '*' + ' ' * 19 + '*')
    # This, you can change the font-size to allow your text to fit in the speech bubble.
    # Next time I will find a way to make the text responsive to the bubble.
    else:
        print(' ' * 3 + '*' + ' ' * 7 + "<span style='font-size:10px;'>" + text + "</span>" + ' ' * 7 + '*')
number = 4
for last in range(4):
    if last == 3:
        print(' ' * 16 + '*' * number)
    else:
        print(' ' * 17 + '*' * number)
    number -= 1
print('''<style>
            img{display:none;}
            body{font-size:95%;}
        </style>''')
>>>>>>> origin/main

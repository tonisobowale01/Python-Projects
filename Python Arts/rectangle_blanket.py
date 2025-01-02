"""
    BroFar's Rectangle Blanket Pattern Challenge.
    Created on February 11, 2023.
    Made by T0N1.
"""
# open('.png', 'w').write('')
for line in range(5):
    for each in range(10):
        if each == 0 or each == 6:
            print('*' * 61)
        elif each == 1 or each == 5:
            print('*' * 5 + ' ' * 7 + '*' * 5 + ' ' * 7 + '*' * 5 + ' ' * 7 + '*' * 5 + ' ' * 7 + '*' * 5 + ' ' * 7
                  + '*')
        elif each == 2 or each == 4 or each == 7 or each == 9:
            print(
                '*' + ' ' * 3 + '*' + ' *' * 4 + ' ' * 3 + '*' + ' *' * 4 + ' ' * 3 + '*' + ' *' * 4 + ' ' * 3 + '*' +
                ' *' * 4 + ' ' * 3 + '*' + ' *' * 4)
        elif each == 3 or each == 8:
            print('*' + ' ' * 3 + '*' + ' ' * 7 + '*' + ' ' * 3 + '*' + ' ' * 7 + '*' + ' ' * 3 + '*' + ' ' * 7 + '*' +
                  ' ' * 3 + '*' + ' ' * 7 + '*' + ' ' * 3 + '*' + ' ' * 7 + '*')
print('*' * 61)
# print('''<style>img{display:none}body{font-size:70%}</style>''')

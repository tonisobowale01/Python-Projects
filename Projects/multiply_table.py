"""
    Multiplication Table.
    Created on June 09, 2023.
    Made by T0N1.
"""
number = int(input('Enter any integer: '))
print('Multiplication Table:')
for no in range(1, 11):
    print(f'{number} x {no} = {number * no}')

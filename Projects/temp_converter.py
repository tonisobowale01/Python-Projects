"""
    Temperature Converter.
    Created on June 12, 2023.
    Made by T0N1.
"""
print("Welcome, you have three options to choose from:\n1. Celsius to Fahrenheit and Kelvin.\n2. "
      "Fahrenheit to "
      "Celsius and Kelvin.\n3. Kelvin to Celsius and Fahrenheit.\n")
print("Now enter either 1, 2, or 3 to continue.")
option = int(input('> '))
if option in {1, 2, 3}:
    user = float(input('Enter degree to be converted: '))

    def temp_converter(a, b):
        # This is to collect the results
        answer = []

        # Celsius Section
        if a == 1:
            fahrenheit = f"{(b * 9 / 5) + 32} ⁰F\n"
            kelvin = f"{b + 273.15} K\n"
            answer.append(fahrenheit + kelvin)
        # Fahrenheit Section
        elif a == 2:
            celsius = f"{(b - 32) * 5 / 9} ⁰C\n"
            kelvin = f"{(b - 32) * 5 / 9 + 273.15} K\n"
            answer.append(celsius + kelvin)
        # Kelvin Section
        elif a == 3:
            celsius = f"{b - 273.15} ⁰C\n"
            fahrenheit = f"{(b - 273.15) * 9 / 5 + 32} ⁰F\n"
            answer.append(celsius + fahrenheit)

        # This is used to iterate over the results in the list, answer.
        for each in answer:
            print(each)

    temp_converter(option, user)
else:
    print('Invalid option.')

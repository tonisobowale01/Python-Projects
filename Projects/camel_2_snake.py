def camel_2_snake(word):

    upper_case = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
                  "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    snake_casing = ''
    word = word[0].lower() + word[1:]
    for letter in word:
        if letter in upper_case:
            letter = '_' + letter.lower()
        snake_casing += letter
    print(snake_casing)


camelCasing = input()
camel_2_snake(camelCasing)

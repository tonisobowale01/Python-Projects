cyan = float(input())
magenta = float(input())
yellow = float(input())
black = float(input())


def rgb(c, m, y, b):
    new = []
    r = 255 * (1 - c) * (1 - b)
    g = 255 * (1 - m) * (1 - b)
    b = 255 * (1 - y) * (1 - b)
    color = [r, g, b]
    for each in color:
        new.append(round(each))
    print(f"{new[0]},{new[1]},{new[2]}")


rgb(cyan, magenta, yellow, black)

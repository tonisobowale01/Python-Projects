"""
    Dice Rolling Simulator.
    Created on June 07, 2023.
    Made by T0N1.
"""

import random
# Get and validate user's input
num_dice_input = input('How many dice do you want to roll? ')


def input_validator(user):
    """This checks if the input is present in a set of numbers between 1 and 6.
    If so, returns an integer of the same value. if not, alerts the user to
    enter a valid number
    """
    if user.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(user)
    else:
        print("Enter a number from 1 to 6.")


num_dice = input_validator(num_dice_input)


def dice_roll(length):
    """This will return a list of generated integers with length num_dice.
    Each integer in the returned list is a random number from 1 to 6.
    """
    results = []
    for num in range(length):
        roll = random.randint(1, 6)
        results.append(roll)
    return results


roll_results = dice_roll(num_dice)

dice_ascii_art = {
    1: ("-----------",
        "|         |",
        "|    *    |",
        "|         |",
        "-----------"),
    2: ("-----------",
        "|   *     |",
        "|         |",
        "|      *  |",
        "-----------"),
    3: ("-----------",
        "|  *      |",
        "|    *    |",
        "|      *  |",
        "-----------"),
    4: ("-----------",
        "|  *   *  |",
        "|         |",
        "|  *   *  |",
        "-----------"),
    5: ("-----------",
        "|  *   *  |",
        "|    *    |",
        "|  *   *  |",
        "-----------"),
    6: ("-----------",
        "|  *   *  |",
        "|  *   *  |",
        "|  *   *  |",
        "-----------")
}
die_height = 5


def die_faces_generator(results):
    """This returns ASCII diagrams of dice faces from roll_results"""
    die_faces = []
    for value in results:
        die_faces.append(dice_ascii_art[value])
    # Then store each line of the dice face in a separate list.
    die_faces_rows = []
    for each in range(die_height):
        rows = []
        for die in die_faces:
            rows.append(die[each])
        die_faces_rows.append(' '.join(rows))
        diagram = '\n'.join(die_faces_rows)
    return diagram


die_face_diagram = die_faces_generator(roll_results)
print(die_face_diagram)

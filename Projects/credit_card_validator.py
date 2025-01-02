<<<<<<< HEAD
def validator(valid: str):
    new = []
    valid = list(map(int, valid[::-1]))
    sec = 1
    while sec < len(valid):
        valid[sec] *= 2
        sec += 2
    for each in valid:
        if each > 9:
            each = each - 9
            new.append(each)
        else:
            new.append(each)
    total = sum(new)
    if len(valid) == 16 and total % 10 == 0:
        print('valid')
    else:
        print('not valid')


cc_number = input()
validator(cc_number)
=======
def validator(valid: str):
    new = []
    valid = list(map(int, valid[::-1]))
    sec = 1
    while sec < len(valid):
        valid[sec] *= 2
        sec += 2
    for each in valid:
        if each > 9:
            each = each - 9
            new.append(each)
        else:
            new.append(each)
    total = sum(new)
    if len(valid) == 16 and total % 10 == 0:
        print('valid')
    else:
        print('not valid')


cc_number = input()
validator(cc_number)
>>>>>>> origin/main

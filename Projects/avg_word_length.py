import math
import string

the_string = list(input())
new = ''
for let in the_string:
    if let in string.punctuation:
        the_string.remove(let)
        continue
    new += let
length = len(new) - new.count(' ')
the_string = list(map(str, new.split(' ')))
word = len(the_string)
print(math.ceil((length / word)))

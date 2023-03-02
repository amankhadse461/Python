
from functools import reduce


def add(s1, s2):
    return s1 + s2
asequence = [1, 2, 3] #add(add(1,2),3)
print(reduce(add, asequence))




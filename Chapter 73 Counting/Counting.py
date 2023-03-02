from collections import Counter
c = Counter(["a", "b", "c", "d", "a", "b", "a", "c", "d"])
print(c)

print(c["a"])

print(c[7])

dict = {'a': 5, 'b': 3, 'c': 5, 'd': 2, 'e':2, 'q': 5}
print(Counter(dict.values()))
 
#: Counting the occurrences of one item in a sequence: list.count() and tuple.count()
list = [1, 2, 3, 4, 1, 2, 1, 3, 4]
print(list.count(1))

tuple = ('bear', 'weasel', 'bear', 'frog')
print(tuple.count('bear'))

print(tuple.count('fox'))


# Counting occurrences in numpy array
import numpy as np
a=np.array([0,3,4,3,5,4,7])
print(np.sum(a==3)) 

#Combinations method in Itertools Module
import itertools 
a = [1,2,3,4,5]
b = list(itertools.combinations(a, 2))
print (b)
b = list(itertools.combinations(a, 3))
print(b)
b = list(itertools.combinations(a, 3))
print(b)

#itertools.dropwhile

def is_even(x):
    return x % 2 == 0
lst = [0, 2, 4, 12, 18, 13, 14, 22, 23, 44]
result = list(itertools.dropwhile(is_even, lst))
print(result)

#Grouping items from an iterable object using a function

lst = [("a", 5, 6), ("b", 2, 4), ("a", 2, 5), ("c", 2, 6)]

def testGroupBy(lst):
    groups = itertools.groupby(lst, key=lambda x: x[1])
    for key, group in groups:
        print(key, list(group))
testGroupBy(lst)     

#itertools.repeat   

for i in itertools.repeat('aman-hey-aman',3):
    print(i)
    
#itertools.count 
for number in itertools.count():
    if number > 20:
        break
    print(number)   


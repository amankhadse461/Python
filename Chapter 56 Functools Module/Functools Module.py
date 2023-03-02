from functools import partial 

def greater_than(a,b):
    return a>b

greater_than =partial(greater_than)
print(greater_than(30,20))
print(greater_than(50,50))
print(greater_than(10,50))
print(greater_than(30,26))
print(greater_than(40,10))
print(greater_than(20,20))
print(greater_than(30,20))

#cmp_to_key
import functools
def mycmp(a, b):
    print("comparing ", a, " and ", b)
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0
  
  
print(sorted([1, 2, 4, 2,3,3,4,2,34,3],key=functools.cmp_to_key(mycmp)))

#reduce
from functools import reduce
def factorial(n):
    return reduce(lambda a, b: (a*b), range(1, n+1))
factorial(10)
from collections import deque
d = deque([1, 2, 3])
p = d.popleft() 
d.appendleft(5) 
print(d)

#Available methods in deque

#Creating empty deque:
d = deque() # deque([]) creating empty deque
print(d)

#Creating deque with some elements:
d = deque([1, 2, 3, 4]) 
print(d)


#Adding element left side of deque:
d.appendleft(0)
print(d)
 

#Adding list of elements to deque:
d.extend([6, 7])
print(d)
 

#Adding list of elements to from the left side:
d.extendleft([-2, -1]) 
print(d)

#Using .pop() element will naturally remove an item from the right side:
d.pop()
print(d)

#Using .popleft() element to remove an item from the left side:
d.popleft()
print(d)

#Remove element by its value:
d.remove(1) 
print(d)

#Reverse the order of the elements in deque:
d.reverse() 
print(d)

#limit deque size

from collections import deque
d = deque(maxlen=3) 
d.append(1) 
d.append(2) 
d.append(3) 
d.append(4) 
print(d)
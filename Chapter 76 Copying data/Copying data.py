#Copy a dictionary
d1 = {1:[]}
d2 = d1.copy()
print(d1 is d2)
 
print(d1[1] is d2[1])
 
 
#Performing a shallow copy
import copy
c = [[1,2]]
d = copy.copy(c)
print(c is d)

print(c[0] is d[0])

#Copy a set 
s1 = {()}
s2 = s1.copy()
print(s1 is s2)

 

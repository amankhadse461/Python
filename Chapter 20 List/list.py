 

lst = []
if not lst:
    print("list is empty")

#Checking whether an item is in a list

li = ["aman","khadse",1,2,1,2,1]
print(li)

'ram' in li

'aman' in li

#Any and All

nums = [1, 1, 0, 1]
all(nums)

chars = ['a', 'b', 'c', 'd']
all(chars)

#"""Concatenate and Merge lists"""

li1 = ["red","black","green","pink"]
print(li1)

li2 = [1,1,1,1,2,5,2,12,5,2,5,2]
print(li2)

for x, y in zip(li1,li2):
    print(x,y)

li1

li1.insert(3,"ram")
print("new list:",li1)

#"""Length of a list"""

l1 = [41,54,24,51552,5,1,5,4,1,45,]
print(l1)

len(l1)

#"""Accessing values in nested list"""

alist = [[[1,2],[3,4]], [[5,6,7],[8,9,10], [12, 13, 14]]]

print(alist[0][0][1])

print(alist[1][1][2])
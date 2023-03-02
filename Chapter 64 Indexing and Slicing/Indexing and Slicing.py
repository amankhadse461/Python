a = "programming language"
print(a[-1])
print(a[:]) 
print(a[::])
print(a[3:]) 
print(a[:4]) 
print(a[2:4])

#Reversing an object
print(a[::-1])

#Slice assignment
lst = [1, 2, 3]
lst[1:3] = [4, 5]
lst[1:4] = [6]
print(lst)

#Making a shallow copy of an array

arr = ['a', 'b', 'c']
copy = arr[:]
arr.append('d')
print(arr) 

#Basic Indexing
arr = ['a', 'b', 'c', 'd']
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[-1])
print(arr[-2])


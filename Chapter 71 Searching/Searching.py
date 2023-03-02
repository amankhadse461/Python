# List
alist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(5 in alist)
print(10 in alist)

# Tuple
atuple = ('0', '1', '2', '3', '4')
print(4 in atuple) 
print('4' in atuple) 

# String
astring = 'i am a string'
print('a' in astring) 
print('am' in astring )
print('I' in astring)

# Set
aset = {(10, 10), (20, 20), (30, 30)}
print((10, 10) in aset)
print(10 in aset) 


def outer_index(nested_sequence, value):
     return next(index for index, inner in enumerate(nested_sequence)
 for item in inner
if item == value)
     
     
a= alist_of_tuples = [(4, 5, 6), (3, 1, 'a'), (7, 0, 4.3)]

print(a)

#Special case: dictionaries

adict = {'a': 3, 'b': 5, 'c': 1}
print(min(adict))
 
print(max(adict))
 
print(sorted(adict))
 
#Using the key argument
list_of_tuples = [(0, 10), (1, 15), (2, 8)]
print(min(list_of_tuples))

#Getting a sorted sequence
print(sorted((7, 2, 1, 5))) 
print(sorted(['c', 'A', 'b']) )
print(sorted({11, 8, 1}) )
print(sorted({'11': 5, '3': 2, '10': 15}))
print(sorted('bdca') )

#Extracting N largest or N smallest items from an iterable
import heapq
print(heapq.nlargest(5, range(10)))
print(heapq.nsmallest(5, range(10)))

#Getting the minimum or maximum of several values 
print(min(7,2,1,5))
print(max(7,2,1,5))
 
#Minimum and Maximum of a sequence
  
print(min([2, 7, 5]))
print(sorted([2, 7, 5])[0])

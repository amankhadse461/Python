#Iteration   
#1
squares = [x * x for x in (1, 2, 3, 4)]
print(squares)

#2
squares = []
for x in (1, 2, 3, 4):
    squares.append(x * x)
    print(squares)
    
##Conditional List Comprehensions 
a =  [x for x in range(10) if x % 2 == 0]
print(a)
a1 = [2 * (x if x % 2 == 0 else -1) + 1 for x in range(10)]
print(a1)

#Dictionary Comprehensions
x ={x: x * x for x in (1, 2, 3, 4)}
print(x)

#List Comprehensions with Nested Loops
data = [[1, 2], [3, 4], [5, 6]]
output = []
for each_list in data:
    for element in each_list:
        output.append(element)
print(output)

#Generator Expressions
x = [x**2 for x in range(10)]
print(x)

for i in [x**2 for x in range(10)]:
    print(i)

#Set Comprehensions
x= {x for x in range(5)}    
print(x)
x ={x for x in range(1, 11) if x % 2 == 0}
print(x)

#Changing Types in a List
items = ["1","2","3","4"]
[int(item) for item in items]
print(items)

#Nested List Comprehensions
x = [x + y for x in [1, 2, 3] for y in [3, 4, 5]]
print(x)
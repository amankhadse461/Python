t = ("aman",454,"khadse")
print(t)

print(type(t))

#Built-in Tuple Functions

tuple1 = ('a', 'b', 'c', 'd', 'e')
tuple2 = ('1','2','3')
tuple3 = ('a', 'b', 'c', 'd', 'e')

print(tuple1, tuple2)

print(tuple2, tuple1)

print(tuple1, tuple3)

#Length
len(tuple1)
len(tuple2)
len(tuple3)

#Max of a tuple
max(tuple1)
max(tuple2)
max(tuple3)

#Min of a tuple
min(tuple1)
min(tuple2)
min(tuple3)

#Convert a list into tuple
list = ['a', 'b', 'c', 'd', 'e']
tuple(list)


#Indexing Tuples
x = (1, 2, 3)
print(x[:-1])  
print(x[-1:]) 
print(x[1:3])  

##Reversing Elements

colors = "red", "green", "blue"
rev = colors[::-1]
colors = rev
print(colors)
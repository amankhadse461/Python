# IS vs  ==
#1
a = "aman"
b = "aman"
a == b
a is b

#2
a = [1, 2, 3, 4, 5]
b = a  
a == b  
a is b  
b = a[:]  
print(a == b)  
print(a is b)  

#3
a = 'short'
b = 'long'
c = 5
d = 5
print(a is b)  
print(c is d)  

## Greater than or less than

#1
x = 20
y = 30 
print(x>y)

#2
x = 20
y = 30 
print(x<y)

# NOT Equal to
#1
12 != 1

#2
12 != '12'

#3
'12' != '12'


# Equal to

a = "aman"
b = "aman"
z = a==b
print("The name of student is :-",z,"aman")
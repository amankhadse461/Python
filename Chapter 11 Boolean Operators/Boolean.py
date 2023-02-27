 # AND
x = True
y = True
z = x and y # z = True
print(z)

x = True
y = False
z = x and y # z = 
print(z)

x = False
y = True
z = x and y # z = False

x = False
y = False
z = x and y # z = False
print(z)


#OR
x = True
y = True
z = x or y # z = True
print(z)

x = True
y = False
z = x or y # z = True
print(z)

x = False
y = True
z = x or y # z = True
print(z)

x = False
y = False
z = x or y # z = False
print(z)

#NOT
x = True
y = not x # y = False
x = False
y = not x # y = True
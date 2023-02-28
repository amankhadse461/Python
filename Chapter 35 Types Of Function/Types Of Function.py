
def cubes(x):
    return x*2
print(cubes(5)) 
  
# Lambda
cubes = lambda x :x*2
print(cubes(2))

#Map

l1 = [1,3,3,3,3,2,1,1,2]

l2 = list(map(cubes,l1))
print(l2)


##filter
def fil(x):
    return x>1
l2 = list(filter(fil,l1))
print(l2)




# Adding types to a function
def add (a,b):
    return a+b
print(add(10,20))
print("aman","khadse")

#Type hints for keyword arguments
def hello_world(greeting: str = 'Hello'):
    print(greeting + ' world!')
    
hello_world()    

#Defining and calling simple functions

def greet():
    print("Hello")
greet()    


def fruits():
    print("mango","orange","banana")
fruits()    

def name():
    print("ram,aman,sameer")
name()    

def do_nothing():
    pass
print(do_nothing())


##Defining a function   

def func(*args):
    for i in args:
        print(i)
func(1, 2, 3) 

##Returning values from functions
def give_me_five():
    return 5
print(give_me_five())

def fruits_name():
    return "mango,apple,banana"
print(fruits_name())


##Nested functions

def fibonacci(n):
    def step(a,b):
        return b, a+b
    a, b = 0, 1
    for i in range(n):
        a, b = step(a, b)
    return a
print(fibonacci(10))


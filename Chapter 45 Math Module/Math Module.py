#ceil 

import math
x=411.5
print(math.ceil(x))

#fabs
#return Absolute value
x = 5521.56
print(math.fabs(x))

#factorial
x = 5
print(math.factorial(x))

#Trigonometry
#length of the hypotenuse
print(math.hypot(2, 4))

#Converting degrees to/from radians
print(math.radians(45))

#Sine, cosine, tangent and inverse functions

# Sine and arc sine
print(math.sin(math.pi / 2))
 
print(math.sin(math.radians(90))) # Sine of 90 degrees
 
print(math.asin(1))
 
print((math.asin(1) / math.pi))
 
# Cosine and arc cosine:
print(math.cos(math.pi / 2))
 
# Almost zero but not exactly because "pi" is a float with limited precision!
print(math.acos(1))
 
# Tangent and arc tangent:
print(math.tan(math.pi/2))

#Logarithms
print(math.log(1))
print(math.log(100))    
print(math.log(100, 10))
print(math.log(27, 3))
print(math.log(1, 10))    


#Constants

from math import pi, e
print(pi)
3.141592653589793
print(e)
2.718281828459045
import cmath
z = 2+3j 
print(cmath.phase(z))  

#Exponential and logarithmic functions

print(cmath.exp(z)) 
print(cmath.log(z)) 
print(cmath.log10(-100))

#Square roots:

print(cmath.sqrt(z))

#Trigonometric functions and their inverses:

print(cmath.sin(z))
print(cmath.cos(z))
print(cmath.tan(z))
print(cmath.asin(z))
print(cmath.acos(z))
print(cmath.atan(z))

#Hyperbolic functions and their inverses
print(cmath.sinh(z)) 
print(cmath.cosh(z))
print(cmath.tanh(z)) 
print(cmath.asinh(z)) 
print(cmath.acosh(z))
print(cmath.atanh(z))
print(cmath.cosh(z)**2 - cmath.sin(z)**2)  
print(cmath.cosh((0+1j)*z) - cmath.cos(z) ) 

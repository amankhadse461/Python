foo = 1
bar = 'bar'
baz = 3.14

print('{}, {} and {}'.format(foo, bar, baz))

#tupe
t = (12, 45, 22222, 103, 6)
print ('{0} {2} {1} {2} {3} {2} {4} {2}'.format(*t))

#Float formatting
print('{0:.0f}'.format(42.12345))

#Named placeholders
data = {'first': 'Aman', 'last': 'Khadse!'}
print('{first} {last}'.format(**data))
from collections import Counter as c
print((c[1,2,1,2,15,15,4,2,4,5,5,2,5,4,5,4545,5,5,4,65]))

print(c('Happy Birthday'))

print(c())

#collections.OrderedDict
d = {'foo': 5, 'bar': 6}
 
print(d)

d['baz'] = 7
print(d)

d['foobar'] = 8
print(d)


from collections import OrderedDict
d = OrderedDict([('foo', 5), ('bar', 6)])
print(d)

d['baz'] = 7
print(d)

d['foobar'] = 8
print(d)


#collections.namedtuple

Person = namedtuple('Person', ['age', 'height', 'name'])

aman = Person(20, 178, 'amankhadse')
print(aman.age) 
print(aman.name) 
from collections import base64
a  ="amankhadse"
b  = a.encode("UTF-8")
print(b)


a  ="amankhadse"
b  = a.encode("UTF-8")
c = base64.b64encode(b)
print(c)

s1 = c.decode("UTF-8")
print(s1)

#Encoding and Decoding Base85
import base64
# Creating a string
s = "hey i am aman!"

b = s.encode("UTF-8")

e = base64.b85encode(b)

s1 = e.decode("UTF-8")

print("Base85 Encoded:", s1)

b1 = s1.encode("UTF-8")

d = base64.b85decode(b1)

s2 = d.decode("UTF-8")
print(s2)
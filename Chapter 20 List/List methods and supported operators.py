a = [1,2,1,2,1,2,1,2,1]
print(a)

#Append
a.append(6)
print(a)

b = ["mango","apple","grapes"]
a.append(b)
    
print(a)


#Extend

a = [1,1,1,5,2,4,2,2,8,2,4,5,5,55]
print(a)
b = [4,4,4,4,4,5,4,4]
a.extend(b)
print(a)

#Index
a.index(5)

#Insert
a.insert(0,"aman")
print(a)

#remove
a.remove(0)
print(a)

#reverse
x = [45,4,5,4,4,5,4,5,4,5]
x.reverse()
print(x)

#count
x.count(4)
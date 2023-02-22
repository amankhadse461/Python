# Types Of Lists

int_list = [1,2,3,4,6,5,]
print(int_list)

string_list = ["aman","khadse"]
print(string_list)

empty_list = []
print(empty_list)


mixed_list = ["aman",12,3.1]
print(mixed_list)

nested_list = [["aman","khadse"],[1,2,3,4,6,5,]]
print(nested_list)

#Accessed  List Element

fruits = ["mango","apple","grapes"]
# print(fruits)
print(fruits[-1])
print(fruits[0])

# Adding element in list
fruits[0] = "banana"
print(fruits)

fruits.append(20)
print(fruits)

fruits.insert(2,"aman")
print(fruits)

fruits.remove("aman")
print(fruits)

fruits.index("apple")

len(fruits)

li= [12,2,3,12,0,12,35,3,3,5,6,3]
li.count(3)

#Tuples

ip_address = ('10.20.30.40', 8080)
print(ip_address)

#Dictionaries

state_capitals = {
 'Arkansas': 'Little Rock',
 'Colorado': 'Denver',
 'California': 'Sacramento',
 'Georgia': 'Atlanta'
}
print(state_capitals)
 

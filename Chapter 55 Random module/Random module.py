import random

l1 = [1,3,4,3,4,3,2,4,53,2]
print(random.choice(l1))

fruits = ("mango",'orange','apple','pineapple')
print(random.choice(fruits))

#shuffle, choice and sample

name = ["aman", "ram", "sham","sammer","hii"]
print(random.shuffle(name)) 

print(random.choice(name))

print(random.sample(name,1))


#randint()
x = 10  
y = 20
print(random.randint(x, y))

#Random Binary Decision

probability = 0.3
if random.random() < probability:
    print("Decision with probability 0.3")
else:
    print("Decision with probability 0.7")
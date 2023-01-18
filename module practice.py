import random
a="abcdef"
print(random.choice(a))

b=[1,2,3,4,5]
random.shuffle(b)
print(b)

print(random.randint(0,10))
for i in range(10):
    random.seed()
    print(random.randint(0,10))
print(random.random())

print(random.randrange(2,10))
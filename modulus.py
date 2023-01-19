# MODULUS
#TYPE 1 -NUMBER AND THEROETIC REPRESENTATIVE FUNCTION
# RANDOM MODULE

import random

#choice(list) function

seq="abcdefghijk"
print(random.choice(seq))

list1=[1,2,3,4,5]
print(random.choice(list1))

#shuffle(list) function(only for list)

list=[1,2,3,4,5]
(random.shuffle(list))
print(list)

#randint(m,n) function - range

output=random.randint(0,10)
print(output)

#seed()-helps to return same random value in multiple iteration

for i in range(10):
    random.seed()
    print(random.randint(1,100))

#random-the function generate a random value from range(0.0,1.0)

print(random.random())

#randrange()-range

print(random.randrange(2,10))

#MATH MODULE

import math

#type 1-number theoretic and representative function

# floor()-round off down value

print(math.floor(2.3))
print(math.floor(2.9))

# ceil()-round off up value

print(math.ceil(2.3))
print(math.ceil(2.1))

# fmod()

print(math.fmod(43.50,4.5))

# fabs()-negative to postive

print(math.fabs(-12.4))

# factorial function

print(math.factorial(3))

#gcd-hcf of as many number

print(math.gcd(1,2,4,5,6,7))

# trunc()-only integer

print(math.trunc(45.567))

#TYPE-2POWER AND ALOGARITHMIC FUNCTION

# exp(),log(),log10(),pow(),sqrt()
import math
print(math.exp(2))
print(math.log(10))
print(math.log10(5))
print(math.pow(2,3))
print(math.sqrt(16))

#TYPE-3 TRIGNOMETRIC FUNCTION-TAKES VALUE IN RADIAN

#sin(x),cos(x),tan(x),hypot(x,y)
print((math.sin(math.radians(30))))
print((math.cos(math.radians(60))))
print(math.tan(math.radians(45)))
print(math.hypot(12,5))

#TYPE-4 ANGULAR CONVERSION FUNCTION

print(math.degrees(1))
print(math.radians(1))

#MATHEMATICAL CONSTANT
# pie,tau,e,inf-infinity

print(math.pi)
print(math.e)
print(math.tau)
print(math.inf)
print(math.nan)

# abs function
print(abs(-12))
print(pow(2,3))#-giving int value
x,y,z=12,13,14
l1=[1,2,3,4,5]
t1=(12,13,14,15,16)
print(max(x,y,z))
print(max(l1))
print(min(t1))
x,y,z=12.520,12.501,12.49
print(round(x))
print(round(x,2))
print(round(y))
print(round(y,2))
print(round(z))

#isinstance-if the value contained in the variable is belonging to the same class as specified in the second parameter of isinstance(
#then it will return true,otherwise false
x,y,z,p=7,3.45,7.8j,"abcd"
print(isinstance(x,int))
print(isinstance(y,int))
print(isinstance(z,complex))
print(isinstance(p,str))


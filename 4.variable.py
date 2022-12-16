_222ts=23
print(_222ts)
a="hello"
b="world"
print(a,b)
value1=value2=23#-chain assignment
print(value1)
print(value2)
print(id(value1))
print(id(value2))#- in python references are made not copies

a=b=c=d=10
print(a,b,c,d)
print(id(a),id(b),id(c),id(d))
x=y=z="hello"
print(x)
print(y)
print(z)
h=29
h+=10
print(h)
x=99
y="hello world"
z="hello python"
print(id(x),id(y),id(z))
print(x,y,z,sep="@")
print("hello",end="  world")
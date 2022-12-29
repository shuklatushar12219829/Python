# first_name="suresh"
# last_name="kumar"
# print("%s %s"%(first_name,last_name))
# a=10
# b=20
# c="tushar"
# d=30.23
# print("the value of a is %d the value of b is %d the value of c is %s the value of d is %.1f"%(a,b,c,d) )
# radius=float(input("Enter the radius"))
# area=3.14*radius**2
# print("the area of give circle is %.3f"%area)
# WIDTH PARAMETER AND FLAG WIDTH
x=123
y=456
# print("%d" %x)
# print("%-5d %d" %(x,y))
# a=3.4567
# print("%5.2f" %a)
# b=45.68542
# print("%10.2f"%b)
# x="hello"
# print("%10s" %x)
# print("%0.2s"%x)
# print("%-10.2s"%x)
# a="teapot"
# # print("%11s"%a)
# print("%-8.3s"%a)
# b=9.8216
# print("%0007.2f"%b)
# a=15
# print("%x"%a)
# print("%X"%a)
# print("%o"%a)
# print("%d"%a)
# a=10
# b=20
# c=30
# print("a:{},b:{}".format(a,b))
# print("{2},{0},{1}".format(a,b,c))

a=10
b=20
print("the value of b is:{1},and the value of a is={0}".format(a,b))
print("{0} {1:d}".format("student",10))
print("{0:5s} is a string".format("abc"))
print("{0:.5s} is a string".format("abcdef"))
print("{0:10.4s} is a string".format("everyone"))
print("{0:>10.4s} is a string".format("everyone"))
print("{0:>3.4f} is a float".format(3.445634974))
print("{0:9s} is a string".format("teapot"))
print("{0:5d} is a integer".format(45))
print("{0:.3s} is a string".format("teapot"))
print("{0:.2f} is a fraction".format(45.125))
print("{0:b} is a binary".format(145))
print("{0:o} is a octadecimal".format(145))
print("{0:x} is a hexadecimal".format(145))
print(format(123.3456,"7.2f"))
print(format("tushar shukla",">8.7"))
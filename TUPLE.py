# CONVERSION TO LIST EDITING AND THEN CONVERTING TO TUPLE
# a=("i","love","python")
# print(a)
# b=list(a)
# b[1]="practice"
# print(tuple(b))
#
# #LIST TO TUPLE
#
# a=[1,2,3,4,5,6]
# print(tuple(a))
#
# a=(1,2,3,[0,7],4)
# a[3][0]=100
# print(a)
# #a[0]=100
# #print(a)--shows error
# print(type(a))
# b=list(a)
# print(b)
# print(type(b))
#
# #CREATING A TUPLE
#
# a=(20,30,40,"apple","ball")
# t1=(1,)
# print(t1)
# print(type(t1))
#
#
# # q=input("values:")
# # r=q.split(",")
# # s=tuple(r)
# # a=int(input("Index:"))
# # if(a<len(s) and a>-len(s)):
# #     print((s[a]))
# # else:
# #     print("Index out of range")
#
# a=("this",10.0,"is","float",3.6)
# print(a[0])
# print(a[1])
# print(a[-1])
# print(a[0:])
# print(a[:-1])
#
# data1=input("Value:")
# a=data1.split(",")
# b=tuple(a)
# x=int(input("number to multiply:"))
# print(b*x)
# data2=input("value2:")
# y=data2.split(",")
# z=tuple(y)
# print(b+z)

# data=input()
# list1=data.split(",")
# a=int(input("Index"))
# b=int(input("value to enter:"))
# list1[a]=b
# c=tuple(list1)
# print(c)

# # SLIDE 37
# data1=input()
# list1=data1.split(",")
# tuple1=tuple(list1)
# a=int(input())
# if a!=-1:
#     if(a<len(tuple1) and a>=len(tuple1)):
#             print(tuple1[:a]+tuple1[a+1:])
#     else:
#         print("Enter valid index")
#     print(tuple1[:a])

# data1=input()
# list1=data1.split(",")
# a=input()
# print(tuple(list1))
# if(a in list1):
#     list1.remove(a)
#     print(tuple(list1))
# else:
#     print("Enter existed elemnt")

# data1=input()
# list1=data1.split(",")
# tuple1=tuple(list1)
# s=int(input("Start index:"))
# e=int(input("end index:"))
# if(s<len(tuple1) and e<len(tuple1) and s>-len(tuple1) and e>-len(tuple1)):
#     print(tuple1[s:e])
# else:
#     print("Enter valid index")

print(any(('','','','')))

data=input()
list1=data.split(',')
tuple1=tuple(list1)
a=input()
count=0
for i in range(0,len(tuple1)):
    if(a == tuple1[i]):
        count=count+1
    else:
        pass
print(count)

data=input()
list1=data.split(",")
tuple1=tuple(list1)
print(tuple1)
element=input()
if element in tuple1:
    index=tuple1.index(element)
    print(index)
else:
    print("Enter existing number")

# list1=list((1,2,3,4,5,6,7))
# print(list1)
#
# list2=list("abcdef")
# print(list2)

# a=input()
# print(type(a))
# print(a.split())
# print(type(a.split()))

# l1=[1,2,3]
# l2=[3,2,1]
# print(l1 == l2)
# print(l1*3)
# print(l1*-1)
# #
# a=input()
# list1=a.split(",")
# print(a.split(","))
# b=int(input("index:"))
# if(b<len(a) and b>=-len(a)):
#     print(list[b])
# else:
#     print("invalid")

# list1=["a","b","c","d"]
# list1[3]="xyz"
# print(list1)

# a=["a","b","c","d"]
# a.append("abcd")#to add new item in the list
# print(a)
#
# a=["a","b","c","d"]
# b=[1,2,3]
# a.extend(b)
# print(a)

list1=["hi","hello","lists"]
print(list1[0],list1[1],list1[2])
list1[2]="python"
print(list1)
list1.append("code is life")
print(list1)
list1.extend([45,67,89])
print(list1)

# # a=input("")
# # b=a.split(",")
# # c=input("")
# # if(c in b):
# #     print("True")
# # else:
# #     print("False")
#
# # a=input()
# # b=a.split(",")
# # if(b[0]=="3" or b[-1]=="3"):
# #     print("True")
# # else:
# #     print("False")
#
# # a=[1,2,3,4,5]
# # a[0:3]=[100,200,300]
# # print(a)
# # a=[1,2,3,4,5]
# # a[0:3]=[]
# # print(a)
# # a=[1,2,3,4,5]
# # a[0:0]=[20,30,40]#inserting of the elements
# # print(a)
# #
# # a=input()
# # b=a.split(",")
# # d=int(input("index:"))
# # c=input("")
# # if(len(b)>d):
# #     b[d]=c
# #     print(b)
# # else:
# #     print("invalid")
#
# # ALIASING-when an existing list is assigned to another variable# for same memory location is used
# # a=[1,2,3,4,5,6]
# # b=a
# # print(a)
# # print(b)
# # print(a is b)
# # print(b is a)
# # a[0]=100
# # print(a)
# # print(b)
# # print(id(a))
# # print(id(b))
# #
# # # CLONING-value remains same but id changes as only slicing is made
# #
# # a=[1,2,3,4,5,6]
# # b=a[:]
# # print(a)
# # print(b)
# # print(a is b)
# # print(b is a)
# # print(id(a))
# # print(id(b))
# # a[0]=100
# # print(a)
# # print(b)
# #
# # # cloning using list function
# # a=[1,2,3,4,5]
# # b=list(a)
# # print(b)
# # print(a)
# #
# # a=[1,2,3,4,5]
# # b=a.copy()
# # print(b)
# # print(a is b)
# #
# # # a=input()
# # # data1=a.split(",")
# # # b=input()
# # # data2=b.split(",")
# # # c=data1[0]
# # # d=data2[0]
# # # e=data1[-1]
# # # f=data2[-1]
# # # print(c == d or e == f )
# #
# # # del to delete an element- permanently removed-deleting memory reference
# # dlist=[1,2,3,4,5,7,6]
# # del dlist[5]
# # print(dlist)
# del dlist[2:]
# print(dlist)
# # delete the value only we can acsess the values
# dlist.clear()
# print(dlist)
# # REMOVE- only removing only first value occurence
# dlist1=[1,2,3,4,5,6]
# dlist1.remove(3)
# print(dlist1)
#
# #IMPORTANT  POP-not only delete the element but return the deleted value-defaultly it remove last element
# dlist2=["red","green","yellow","cyan"]
# elem=dlist2.pop()
# print(elem)
# elem=dlist2.pop(-1)
# print(elem)
#
# # w=input()
# # q=w.split(",")
# # list1=[]
# # for i in range(len(q)):
# #     if q[i] not in list1:
# #         list1.append(q[i])
# # print(q)
# # print("after removing duplicates",list1)
#
# #FUNCTION
# # 1. all()-check all the value of list any value giving ascii code is true
# print(all([False,",","1","2"]))
# print(all([]))
# print(all([0,",","1","2"]))
#
# # 2. any()-any one value is true then over all value is true
# print(any([' ',',','1',False]))
# print(any([0]))
#
# # 3. enumerate()- gives pair of tuple starting from zero
# print(list(enumerate(['a','b','c','d','e'])))#result will be a function composition
#
# # 4. len()-length for the list
# a=[1,2,3,4,5,6]
# print(len(a))
#
# # 4. list-convert to list
# # a=input()
# # print(list(a))
#
# # 5. max- maximum value of the list
# a=[1,2,3,4,2,3,4,6,4,4,3,4,4,6,3,4]
# print(max(a))
#
# # 6. min-minimum value of the list
# a=[1,2,3,2,4,54,6,4,4.6,4,5,64,64,65]
# print(min(a))
#
# # 7. sorted-ordered list-makes a new list
# a=[3,32,2,5,7,45,3,3,7,8,9]
# b=sorted(a)
# print(b)
# print(b[-1::-1])
#
# # # 8. sum- sum of all the value in the list |condition|: of same type
# # a=[1,2,3,4,5,6,7]
# # print(sum(a))
# # #STUDY ABOUT BUBBLE SORT
# #
# # # a=input("data:")
# # # b=a.split(",")
# # # print(b)
# # # c=int(max(b))
# # # d=int(min(b))
# # # print("max:",c)
# # # print("min:",d)
# # # print("difference:",c-d)
# #
# # # data1=input()
# # # data2=input()
# # # list1=data1.split(",")
# # # list2=data2.split(",")
# # # a=""
# # # if(len(list1)==len(list2)):
# # #     for i in range(0,len(list1)):
# # #        a=a + list1[i] + ":" + list2[i]
# # #     print("{",a,"}")
# # # else:
# # #     print("length is not equal")
# # #
# #
# # # a=input()
# # # b=input()
# # # list1=a.split(",")
# # # list2=b.split(",")
# # # list3=[]
# # # if(len(a)==len(b)):
# # #     for i in range(0,len(list1)):
# # #         a=abs(int(list1[i])-int(list2[i]))
# # #         list3.append(a)
# # #     print(list3)
#
# # INSERT-insert value at any index
# x=['a','b','c','d']
# x.insert(0,1)
# print(x)
#
# a=[1,2,3,4,5,56,4,32,2]
# print(a.count(2))
#
# # SORT- ascending order
#
# x=[1,2,3,32,2,3,4,53,2,11]
# x.sort(key=None, reverse=True)
# print(x)
# x.sort(key=None, reverse=False)
# print(x)
#
# # Reverse-
# x.reverse()
# print(x)
#
# # COPY-return shallow copy
# x=[2,3,1,2,3,2,3,4]
# y=x.copy()
# print(y)
# w=input()
# count=0
# list1=x.split(",")
# a=int(input())
# b=len(list1)
# for i in range(0,b):
#     if(w==y[i]):
#         count=count+1
# print(w,count)

#BINARY SEARCH-list to be sorted
# data=input()
# list1=data.split(",")
# count=0
# a=input()
# for i in range(0,len(list1)):
#     if(a==list1[i] and list1[i]==list1[i+1]):
#         result="True"
#         break
#     else:
#         result="False"
# print(result)

# a=input()
# b=input()
# list1=a.split(",")
# count=0
# list2=b.split(",")
# c=len(list1)
# for i in range(0,len(list1)):
#     for j in range(0,len(list2)):
#         if(list1[i]==list2[j]):
#             count=count+1
#         else:
#             pass
# if(count==len(list1)):
#     print("Exist")
# else:
#     print("Not exist")

# cap=input("enter A in upper case:")
# small=input("enter a in lower case")
# i=ord(cap)
# j=ord(small)
# alpha=[]
# for k in range(26):
#     alpha.append(chr(i))
#     alpha.append(chr(j))
#     i=i+1
#     j=j+1
# print(alpha)
# print(sorted(alpha))

# data=input()
# list1=data.split(",")
# count=0
# list2=sorted(list1)
# for i in range(len(list1)):
#     if(list1[i]==list2[i]):
#         count=count+1
#     else:
#         pass
# if(count==len(list1)):
#     print("True")
# else:
#     print("False")

# a=input("Please enter a sentence")
# x=a.lower()
# b=x.split(",")
# c=sorted(b)
# alpha=[]
# count=0
# for i in range(len(c)):
#     if(c[i] not in alpha):
#         print(alpha.append(c[i]),count(c[i]))
#     elif(c[i] in alpha):
#         count=count+1
#         print(alpha.append(c[i]),count(c[i]))
#ALIASING
a=[1,2,3,4,5,6]
b=[1,2,3,4,5,6]
b=a
print(a is b)
print(b is a)
a[0]=100
print(a)
print(b)
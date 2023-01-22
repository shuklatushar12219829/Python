# #Dictionary are in the form of key value pair
# month={"jan":1,"feb":2,"mar":3,"apr":4,"may":5,"jun":6,"jul":7}
# print(month["jan"])# indexing
# #print(month["dec"])# key error
# print(month.get("jan"))#doesnot show error if key is not in the dictionary
# print(month.get("nov"))
# print(month.get("sep","Not available"))
# month=[("jan",1),("feb",2),("mar",3)]
# print(dict(month))
#
# dict1={"name":"tushar","number":226,"age":17}
# for i in dict1:
#     print(dict1[i])
# for i ,j in dict1.items():
#     print(i,j)
# print(dict1.keys())
# print(dict1.values())
#
# dict2={"name":"tushar","number":226,"age":17}
# print(dict2)
# dict2["name"]="prakhar"
# print(dict2)
#
# #
# #item methods :it returns list of pair of tuples
# dict1={"cyan":1,"red":2,"green":3}
# dict2={"light":4,"pink":6}
# print(dict1.update(dict2))
#
# data1=input()
# data2=input()
# list1=data1.split(",")
# list2=data2.split(",")
# d1={}
# if(len(list1)==len(list2)):
#     for i in range(len(list1)):
#         d1[list1[i]]=list2[i]
#     print(sorted(d1.items()))
# else:
#     print("Length should be equal")
#
# d1=input()
# d2=input()
# l1=d1.split(",")
# l2=d2.split(",")
# a=input()
# dict1=dict(zip(l1,l2))
# print(dict1.get(a))
#
# data1=input()
# data2=input()
# list1=data1.split(",")
# list2=data2.split(",")
# dict1=dict(zip(list1,list2))
# a=input()
# if a in dict1:
#     print("True")
# else:
#     print("False")

# data1=input()
# data2=input()
# list1=data1.split(",")
# list2=data2.split(",")
# d1={}
# if(len(list1)==len(list2)):
#     for i in range(len(list1)):
#         d1[list1[i]]=list2[i]
#     print(sorted(d1.items()))

fruits={1:"apple",2:"grapes",3:"mango",4:"chiku"}
#POP function
print(fruits.pop(4))
print(fruits)
print(fruits.popitem())
print(fruits)
#DEl function-delete the key for which index is given
# del fruits[1]
# print(fruits)
# #CLEAR -clears the dictionary
# fruits.clear()
# print(fruits)
#
# d1=input()
# d2=input()
# l1=d1.split(",")
# l2=d2.split(",")
# dict1=dict(zip(l1,l2))
# a=input()
# if(a in dict1):
#     print(dict1.pop(a))
#     sorted_dict=sorted(dict1.items())
#     print(sorted_dict)
# else:
#     print("Input corect value")
#
# data1=input()
# data2=input()
# list1=data1.split(",")
# list2=data2.split(",")
# dict1=dict(zip(list1,list2))
# l1=[]
# for key in dict1:
#     l1.append(dict1[key])

# d1=input()
# d2=input()
# l1=d1.split(",")
# l2=d2.split(",")
# d1=dict(zip(l1,l2))
# key=input()
#
# if(key in d1):
#     value = input()
#     d1[key]=value
#     print(d1)
#
# else:
#     print("enter valid ")

# dict1={'jan':1,'feb':2,'mar':3,'apr':4,'may':5}
# print(dict1.items())
# dict2=[('jan',1),('feb',2),('mar',3),('apr',4),('may',5)]
# print(dict(dict2))
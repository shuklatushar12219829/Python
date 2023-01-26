# a="this is my first string"
# print(a)
# print(a[11])
# print(a[-6])
# lang="python"
# print(lang[0:])
# print(lang[:6])
# b="PYTHON"
# print(b[0:4])
# print(b[:3])
# print(b[::-1])
# print(b[-1::-3])
# print(b[4:1:-1])
# print(b[4:1:1])#NOT LOGICAL
# print(b[2:5:-1])
# a="String is how are you?"
# print(a[14:17])
# print(a[12:15])
# print(a[-4:-1])
# print(a[-2:-5:-1])
# print(a[-4:])
# a=input()
# if(len(a)>2):
#     print(a[:2]+a[-2:])
# else:
#     print("output:",str)
# b=input("a:")
# print(b[1:-1])
# str=input("a:")
# b=str[0]
# c=str[-1]
# if(len(str)>1):
#     print(c+str[1:-1]+b)
# elif(len(str)==1):
#     print(str)
# elif(len(str)==0):
#     print("Null")
# str1=input()
# str2=input()
# print(str1+str2+str2+str1)
# print(str1+str2+str1[::-1]+str2[::-1])

# a=input()
# num=int(input())
# print(a[:num]+a[num+1:])
#
# a=input("a:")
# b=input("b:")
# c=a[1:]+b[1:]
# if(len(c)>0):
#     print(c)
# else:
# #     print("Null")

# s="good morning"
# print("m" in s)
# print("good" in s)
# print(3 * s)#expression * string
# str=input("str:")
# print(4*str)
# print(3*str[::-1])

# a=input()
# if(len(a)>=3):
#     print(a[0:3]*3)
# else:
#     print(a)
#
# a=input("str:")
# num=int(input("num:"))
# if(num>=0 and num<len(a)):
#     print("result:",a*num)
# else:
#     print("num should be positive ,less than length of the str")

#                                          immutable nature of string
#
# a="python"
# print('j'+a[1:])
# #use of del for deleting a string
# del a
# print(a)

#                                           INBUILD STRING METHOD
a="welCoMe tO PyThon"
x="Hello"
print(a.capitalize())#first letter to capital
print(a.upper())#all the letter  to upper case
print(a.lower())#all the letter to lower case
print(a.title())#first word of each letter to captial
print(a.swapcase())#capital to small and vice-versa
print(a.split())#convert string to list
print(a.split('M'))#convert string to list
print(a.center(150,"$"))# move to string to centre of the screen  a.center(width,fillchar)
print(a.isnumeric())#if numeric gives true both interger and float
b="happy married life happy birthday birthday baby"
print(b.count('h'))#number of times character is in string
print(b.replace("happy","sed"))#old substring to new sub string
c="."
d="koc36"
l1=["www","google","com"]
print(c.join(l1))#list to string
print(b.isupper())#checks whether string is in upper case or not
print(b.islower())#checks whether string is in lower case or not
print(b.isalpha())#checks whether the string is in alphabet or not
print(x.isalpha())#checks whether the string is in alphabet or not
# HW BUILD ALL THE BUILD IN FUNCTION
print(d.isalnum())#checks whether the given is alpha number or not)
print(d.isdigit())#checks whether the give is digit or not only the integer
print(a.isspace())#true when the string is space string
print(x.istitle())#first letter of all words are capital or not


# #                                          escape character
# print("hello\npython")
# print("hello\"everyone")
# str="hello\npython"
# print(str)
# #for printing \n and \r
# print(repr(str))

# str1=input()
# str2=input()
# if(len(str1)>len(str2)):
#     print(str2+str1+str2)
# elif(len(str1)<len(str2)):
#     print(str1+str2+str1)
# else:
#     print("same length")

# p="hello python"
# print(p.startswith("hell"))
# p="hello python"
# print(p.endswith("w"))
# p="hello python"
# print(p.find("th"))#to find the index of the required substr in the str
# q="hello python hello"
# print(q.find("hey"))
# print(len(q))
# print(min(p))
# print(max(p))

# r=input("str:")
# if(r.startswith("Python") and r.endswith("Programming")):
#     print("valid")
# else:
#     print("invalid")
# print(max(r))
# print(min(r))

#                                       STRING MODULUS
import string
# print(string.punctuation)
# print(string.digits)
# print(string.printable)#all the character that can be print
# print(string.capwords('hello python'))#works like title
# print(string.hexdigits)
# print(string.octdigits)
#
# a=input("str:")
# b=input("str2:")
# print(a.count(b))
#                                       HW    slide 70
#
#                                       HW    use def of count function
# str=input("str:")
# ret=""
# for i in str:
#     ret=ret+2*i
# print(ret)

# a=input()
# b=len(a)
# c=b/2
# if(len(a)%2==0):
#     print(a[0:c+1])
# else:
#     print(a[c+1:])
#
# str=input("str:")
# if(len(str)>0):
#     print("first",str[0::2])
#     print("second",str[1::2])
# else:
#     print("null")

# a=input("str:")
# length=len(a)
# result=""
# for s in range(0,length+1):
#     result=result+a[:s]
# print(result)

# a="python\nis good"
# print(a.isprintable())
# import string
# for i in string.ascii_letters:
#     print(i,"\t\t",ord(i))

a=input("str:")
b=sorted(a)
printed=[]
for char in b:
    if(char not in printed):
        print("'{0}'\t{1}".format(char,b.count(char)))
        printed.append(char)
print(printed)

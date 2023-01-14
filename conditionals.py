a=int(input("Enter the number:"))
if(a>3):
    if(a==4):
        print("a is 4")
    print("a is greater than 3")
elif(a>2):
    print("a is greater than 2")
elif(a>1):
    print("a is greater than 1")
else:
    print("a is zero")
print('done')

# # x=int(input("enter the number:"))
# # if (x>0):
# #     print("x is a postive number")
# # else:
# #     print("x is negative number")
# # print("how are you")
#
# # y=int(input("number:"))
# # if(y%2==0):
# #     print("number is even")
# # else:
# #     print("number is odd")
#
# # age=int(input("age:"))
# # if(age>=18):
# #     print("you are eligible to vote")
# # else:
# #     print("you are not eligible to vote")
#
# # a=int(input("Enter a number:"))
# # if(a%7==0):
# #     print("Given",a,"is divisble","by 7")
# # print("End of the program")
#
# # a=27
# # b=27.0
# # if(a==b):
# #     print("a and b are equal")
# #     if(a!=b):
# #         print("a and b are not equal")
#
# # marks=int(input("Enter marks obtained:"))
# # if(marks>75):
# #     print("User secured distinction")
# # else:
# #     print("User did not secured distinction")
#
# # balance=int(input("Enter the balance in your account:"))
# # if(balance>=1000):
# #     print("sufficient balance")
# # else:
# #     print("balance is low")
#
# # x=int(input("Enter a number:"))
# # if(x>0):
# #     if(x%5==0):
# #         print("x is multiple of 5")
# #     else:
# #         print("x is not mutiple of 5")
# # else:
# #     print("x is negative")
#
#
# # a=int(input("Enter a number:"))
# # if(a==0):
# #     print("number is zero")
# # elif(a>0):
# #     print("positive")
# # else:
# #    print("negative")
#
# # x=int(input(""))
# # y=int(input(""))
# # if(x>y):
# #     print(x,"is greater than",y)
# # elif(x<y):
# #     print(x,"is smaller than",y)
# # else:
# #     print(x,"is equal to",y)
#
# #score=int(input("score:"))
# # if(score>90):
# #     print("A")
# # elif(score>80):
# #     print("B")
# # elif(score>70):
# #     print("C")
# # elif(score>60):
# # #     print("D")
# # # else:
# # #     print("F")
# #
# # a=int(input("num1:"))
# # b = int(input("num2:"))
# # c = int(input("num3:"))
# # if(a>b and a>c):
# #     print(a,"is greatest")
# # elif(b>a and b>c):
# #     print(b,"is greatest")
# # elif(c>a and c>b):
# #     print(c,"is greatest")
# # # HW-compute roots of a quardratic  equation
# # a=int(input("a="))
# # b=int(input("b="))
# # c=int(input("c="))
# # d=b**2-4*a*c
# # if(d>0):
# #     print("real roots")
# # elif(d<0):
# #     print("equal roots")
# # else:
# #     print("imaginary roots")
#
# # a=input("Enter any character:")
# # if(a==0):
# #     exit()
# # elif((a>="A" and a<="Z") or (a>="a" and a<="z")):
# #     print(a,"is aphabet")
# # elif(a>='1' and a<='2'):
# #     print(a,"is a digit")
#
# # year=int(input("year:"))
# # if(year%4==0 and year%100!=0):
# #     print("yes a leap year")
# # elif(year%400==0 ):
# #     print("yes is a leap year")
# # else:
# #     print("not a leap year")
# # electric bill()error
# # print("1-100 unit-1.5/-")
# # print("101-200 unit-2.5/-")
# # print("201-300 unit-4/-")
# # print("301-350 unit-5/-")
# # print("350 and above unit-15/-")
# # units=int(input("number of units-"))
# # if(units>350):
# #     print(float(100 * 1.5 + (units-100) * 15))
# # elif(units>301):
# #     print(float(100 * 1.5 + (units - 100) * 5))
# # elif (units > 201):
# #     print(float(100 * 1.5 + (units - 100) * 4))
# # elif (units > 101):
# #     print(float(100 * 1.5 + (units - 100) * 2.5))
# # elif (units > 1):
# #     print(float(units * 1.5 ))
#
# # a=int(input("Side 1:"))
# # b=int(input("Side 2:"))
# # c=int(input("Side 3:"))
# # if(a==b==c):
# #     print("Equilatoral triangle")
# # elif(a==b!=c or b==c!=a or a!=c==a):
# #         print("isosceles triangle")
# # else:print("scalene triangle")
#
# #H.W
# #BMI calculator
# # tds calculator as per the current slab
# #
# # str1=input("Enter str")
# # str2=input("Enter str")
# # if(str1>str2):
# #     print(str1,"is greater")
# # elif(str1<str2):
# #     print(str2,"is greater")
# # else:
# #     print(str1,"is equal to",str2)
#
# weight=float(input("Weight(in pound):"))
# height=float(input("Height(in inches):"))
# a=weight*.45359237
# b=height*.0254
# bmi=a/b**2
# if(bmi<18.5):
#     print("under weight")
# elif(bmi<25):
#     print("Normal")
# elif(bmi<30):
#     print("Overweight")
# else:
#     print("obese")
#
#
#
#
#
#
#
# num1=int(input(""))
# num2=int(input(""))
# max=num1 if num1>num2 else num2
# print(max)

num=int(input("Enter a number:"))
max="number is even"if num%2==0 else"not even"
print(max)
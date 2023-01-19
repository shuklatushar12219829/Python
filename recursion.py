# #factorial
# def recurfact(n):
#     if(n==1 or n==0):
#         return 1
#     else:
#         return n*recurfact(n-1)
# num=int(input("num: "))
# if(num<0):
#     print("factorial not exist")
# else:
#     print("factorial:",recurfact(num))
# # sum of n number
# def resur(n):
#     if(n==1 or n==0):
#         return n
#     else:
#         return n+resur(n-1)
# num=int(input("num:"))
# print("factorial",resur(num))

# reverse

# def reverse(n,x):
#     if(n==0):
#         return x
#     x=(x*10)+(n%10)
#     return reverse(n//10,x)
# num=int(input("x:"))
# print(reverse(num,0))

def fibb(n):
    if(n<=1):
        return n
    else:
        return(fibb(n-1)+fibb(n-2))
n=int(input("Enter the maximum limit to generate the fibonnaci series:"))
print("the fibonacci series:" )
for i in range(0,n):
      print(fibb(i))
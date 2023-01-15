#HELLO

# for i in range(5):
#     for i in range(2):
#                    print("Hello")

#TABLES

# print("Multiplication table")
# print(" |",end="")
# for j in range(1,11):
#     print(" ",j,end="")
# print()
# print("---------------------------")
# #displaying the table
# for i in range(1,11):
#     print(i,"|",end="")
#     for j in range(1,11):
#         print(format(i * j,"4d"),end="")
#     print()

#PATTERN 1

# for i in range(6):
#     for j in range(6):
#         print("*",end="")
#     print()

#PATTERN 2
# n=1
# m=int(input("no:"))
# for i in range(m):
#     for j in range(n):
#         print("*",end="")
#     n=n+1
#     print()

#PATTERN 3

# m=int(input("r"))
# n=int(input("c"))
# a=1
# for i in range(m):
#     for j in range(a,n+1):
#         print("*",end="")
#     print()

#PATTTERN

# n=int(input("n:"))
# for i in range(n):
#     for j in range(n):
#         print("*",end='')
#     n=n-1
#     print()

#HW
# 1)@@@@@
#   ####
#   @@@
#   ##
#   @
# n=5
# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         if(i%2!=0):
#             print("@",end="")
#         else:
#             print("#",end="")
#     n=n-1
#     print()
# 2) 54321
#    5432
#    543
#    54
#    5
n=1
for i in range(1,6):
    for j in range(5,n-1,-1):
        print(j,end=" ")
    n=n+1
    print()
# 3) 55555
#    4444
#    333
#    22
#    1
# n=5
# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         print(n,end="")
#     n=n-1
#     print()
# 4)1
#   12
#   123
#   1234
#   12345
n=1
for i in range(1,6):
    for j in range(1,n+1):
        print(j,end=" ")
    n=n+1
    print()
# 5)13579
#   1357
#   135
#   13
#   1
n=5
for i in range(1,6):
    for j in range(1,2*n,2):
        print(j,end=" ")
    n=n-1
    print()

#6) a
#   ab
#   abc
#   abcd
#   abcde
var=96
n=97
for i in range(1,7):
    for j in range(var,n):
        print(chr(j),end="")
    n=n+1
    print()
#7) a
#   bb
#   ccc
#   dddd
#   eeeee
v=97
n=98
b=122
for i in range(1,6):
        print(i*chr(v),end=" ")
        v=v+1
        print()


# val=65
# n=int(input("no of rows:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(val),end="")
#         val=val+1
#     val=65
#     print()
# PRIME NUMBER
# flag=0
# n=int(input("enter n(>=2)"))
# m=int(input("enter m(>=2)"))
# print("list number of prime number:")
# for i in range(n,m+1):
#     for j in range(2,(i//2)+1):
#         if(i%j==0):
#             flag=1
#     if(flag==0):
#         print(i)
#     flag=0

#MATRIX TRANSPOSE

# matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# matrix1=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
# print("matrix:",matrix)
# for i in range(3):
#     for j in range(4):
#         matrix1[j][i]=matrix[i][j]
# print("transposed:",matrix1)

# BREAK STATEMENT
#
# num=10
# i=1
# while(i<=num):
#     print(i)
#     i=i+1
#     if(i%5==0):
#         break
#     else:print(num)

# CONTINUE STATEMENT

# for i in range(1,10):
#     if(i%2==0):
#         continue
#     print(i)


# for i in range(1,20):
#     if(i<=10):
#         continue
#     print(i)
#*
#* *
#* * *
#* * * *
#* * * * *
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
# n=7
#     *
#    **
#   ***
#  ****
# ****
n=7
for i in range(1,6):
    for j in range(1,n):
     if(i<j):
        print("*",end="")
     elif(i<=j):
        print(" ",end=" ")
    print()
# #* * *
# #* * *
# for i in range(3,4):
#     print(i * "*")
#     print(i * "*")
# # # # #
# # # # #
# # # # #
# # # # #
# for r in range(0,4):
#     for c in range(0,3):
#         print("#",end=" ")
#     print()
# # 1 0 0 0
# # 0 1 0 0
# # 0 0 1 0
# # 0 0 0 1
# for i in range(0,4):
#     for j in range(0,4):
#         if(i==j):
#             print("1",end=" ")
#         elif(i!=j):
#             print("0",end=" ")
#     print()
# #1 0 0 1
# #0 1 1 0
# #0 1 1 0
# #1 0 0 1
# for i in range(1,5):
#     for j in range(1,5):
#         if(i+j==5 or i==j):
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print()
# #1111
# #0000
# #1111
# #0000
# for i in range(0,4):
#     for j in range(0,4):
#         if(i%2==0):
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print()
# #1 0 1 0 1 0 1
# #1 0 1 0 1 0 1
# #1 0 1 0 1 0 1
# for i in range(0,3):
#     for j in range(0,7):
#         if(j%2==0):
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print()
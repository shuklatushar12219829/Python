# # nested list comprehension
# print([a*b for a in [1,2,3] for b in [10,20,30]])
# print([a for a in [10,8,5,4] for b in [4,7,5,10] if a!=b])#thus proved it checkes for every value
# print([a for a in [10,8,5,4] for b in [4,7,5,10] if a==b])
# print([a for a in range(0,50) if a%2==0 if a%3==0])
# #                        or
# print([a for a in range(0,50) if a%6==0])
#
# #Matrix operation
# matrix=[[1,2,3,4],[5,6,7,8],[9,10,20,13]]
# transposed=[]
# print("matrix:")
# print(matrix)
# """Matrix transpose using nested while"""
# i=0
# while i<len(matrix[0]):
#     j=0
#     lx=[]
#     while(j<len(matrix)):
#         lx.append(matrix[j][i])
#         j=j+1
#     transposed.append(lx)
#     i=i+1
# print(transposed)
#
#
# matrix=[[1,2,3,4],[5,6,7,8],[9,10,20,13]]
# transposed=[]
# print("matrix:")
# print(matrix)
# """Matrix transpose using nested for"""
# for i in range(len(matrix[0])):
#     lx=[]
#     for j in matrix:
#         lx.append(j[i])
#     transposed.append(lx)
# print(transposed)
#
# matrix=[[1,2,3,4],[5,6,7,8],[9,10,20,13]]
# transposed=[]
# print("matrix:")
# print(matrix)
# """Matrix transpose using single list comprehension"""
# for i in range(len(matrix[0])):
#     transposed.append([row[i] for row in matrix])
# print(transposed)
#
# matrix=[[1,2,3,4],[5,6,7,8],[9,10,20,13]]
#
# print("matrix:")
# print(matrix)
# """Matrix transpose using double list comprehension"""
# transposeded=[[row[i] for row in matrix] for i in range(len(matrix[0]))]
# print(transposeded)

#matrix multiplication by nested for
#addition of two matrix
#subtraction of two matrix
#division of two matrix
#sum of diagonal

# list1=[int(x) for x in input("data: ").split(",")]
# print("content:",list1)

#dry run of spars matrix

#dictionary comprehension

#{key : value (key , value) in iterable}
list1=[10,20,30]
dict1 = {key: value for key , value in enumerate(list1)}
print(dict1)

dict2={i:i**2 for i in range(1,11)}
print(dict2)

dict3={k:"python" for k in "codetantra"}
print(dict3)

dict4={i.lower():i for i in "PYTHON"}
print(dict4)


ordchar={x:chr(x) for x in range(65,91)}
charord={x:y for y,x in ordchar.items()}
print(sorted(ordchar.items()))
print(sorted(charord.items()))


#sparse matrix=[[],[],[]] First row -row's for all non-zero element,second row -number of column for all non zero element
#Third for non zero element
def sparseMatrix(sparseMatrix, m, n):
	# initialize size as 0
	size = 0
	for i in range(m):
		for j in range(n):
			if (sparseMatrix[i][j] != 0):
				size += 1

	# number of columns in compressMatrix(size) should
	# be equal to number of non-zero elements in sparseMatrix
	rows, cols = (3, size)
	compressMatrix = [[0 for i in range(cols)] for j in range(rows)]

	k = 0
	for i in range(m):
		for j in range(n):
			if (sparseMatrix[i][j] != 0):
				compressMatrix[0][k] = i
				compressMatrix[1][k] = j
				compressMatrix[2][k] = sparseMatrix[i][j]
				k += 1

	print("Sparse representation:")
	for i in compressMatrix:
		print(i)
a=int(input("Enter row size:"))
b=int(input("Enter col size:"))
print("Enter elements:")
mat=[[int(input()) for x in range(b)] for y in range(a)]
print("Sparse matrix is:")
for i in range(a):
    for j in range(b):
        print(mat[i][j],end=" ")
    print()
sparseMatrix(mat,a,b)


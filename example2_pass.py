class Student:
	pass
Stud_1 = Student()#<object name>=constructor()-->it is a special method which has same name as that of class
Stud_2 = Student()
Stud_1.name = input('s1 name: ')
Stud_1.age = int(input('s1 age: '))
Stud_1.graduate = input('s1 degree: ')
Stud_2.name = input('s2 name: ')
Stud_2.age = int(input('s2 age: '))
Stud_2.graduate = input('s2 degree: ')
print("Stud_1.name:", Stud_1.name)
print("Stud_1.age:", Stud_1.age)
print("Stud_1.graduate:", Stud_1.graduate)
print("Stud_2.name:", Stud_2.name)
print("Stud_2.age:", Stud_2.age)
print("Stud_2.graduate:", Stud_2.graduate)
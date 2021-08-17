class Student:
  dept='BCA'  #define class
  def __init__(self,name,age):
    self.name=name         #instance variable
    self.age=age             #instance variable


#define the object of student class
stud1=Student('ANU', '22')
stud2=Student('ANKIT' , '19')

print(stud1.dept)
print(stud2.dept)
print(stud1.name)
print(stud2.name)
print(stud1.age)
print(stud2.age)
 

#access class variable using the class Name
print(Student.dept)
 
 #change the department of particular isinstance
stud1.dept='Networking'
print(stud1.dept)
print(stud2.dept)

#change  the department for all instance of class
Student.dept='Database Administration'
print(stud1.dept)
print(stud2.dept)


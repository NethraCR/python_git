class Student:

    marks=[]
    def get_data(self,id,name,m1,m2,m3):
        Student.id=id
        Student.name=name
        Student.marks.append(m1)
        Student.marks.append(m2)
        Student.marks.append(m3)

    def displayData(self):
        print("ID:",Student.id)
        print("Name:",Student.name)
        print("Marks are:",Student.marks)

    def total(self):

        return(Student.marks[0]+Student.marks[1]+Student.marks[2])

id=int(input("Enter id:"))
name=input("Enter name:")
m1=int(input("Enter the marks in 1st sub:"))
m2=int(input("Enter the marks in 2nd sub:"))
m3=int(input("Enter the marks in 3rd sub:"))

s1 = Student()
s1.get_data(id,name,m1,m2,m3)
s1.displayData()
print("the total marks :",s1.total())


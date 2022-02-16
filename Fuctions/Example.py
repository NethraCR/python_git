class Student:

    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age

    def student(self):
        print("Student Name :{}".format(self.name))
        print("Student Id:{}".format(self.id))
        print("Student Age :{}".format(self.age))
J = Student("Nani", 123, 17)
J.student()








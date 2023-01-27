class Student:
    pass
class Marks:
    pass
Student_1 = Student()
Student_2 = Student()
marks_1 = Marks()
marks_2 = Marks()
print(isinstance(Student_1, Student))
print(isinstance(Student_2, Student))
print(isinstance(marks_1, Marks))
print(isinstance(marks_2, Marks))
print(issubclass(Student, object))
print(issubclass(Marks, object))
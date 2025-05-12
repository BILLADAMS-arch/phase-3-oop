class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def course_average(self):
        count = 0
        for student in self.students:
            count += student.marks
        print(count / len(self.students))


student1 = Student("Alice", 20, 85)
student2 = Student("Bob", 22, 78)
student3 = Student("Charlie", 21, 92)


math = Course("Python")
math.add_student(student1)
math.add_student(student2)
math.add_student(student3)


math.course_average()


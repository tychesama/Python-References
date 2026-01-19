from OOP import Student
class WorkingStudent(Student):
    def __init__(self, newName, newGrades, newSalary):
        super().__init__(newNames,newGrades)
        self.salary = newSalary

    def getAverage(self):
        return sum(self.grades) / len(self.grades)

st_two = Student("Hello World", [90,85,80,98])


print(st_two.getAverage())
print(Student.student_count)

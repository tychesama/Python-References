class Student:
    student_count = 0
    def __init__(self, newName, newGrades):
                 self.fullName = newName
                 self.grades = newGrades
                 Student.student_count += 1
    def getAverage(self):
        return sum(self.grades) / len(self.grades)

    
st_one = Student("Joem Idpan", [77,74,80,98])

print(st_one.getAverage())
print(Student.student_count)

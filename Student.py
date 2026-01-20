from per import Person

class Student(Person):
    def __init__(self, idNum, fullName, gender, grades):
        super().__init__(idNum,fullName, gender)
        self.grades = grades

    def getStudent(self):
        return f"{self.idNum} | {self.fullName} | {self.gender} | {self.grades}"

person = Person("1233332231", "Joem2", "maleee")
stud = Student("1233332231", "Joem3", "maleee231", "80")

print(person.getPerson())
print(stud.getStudent())
from per import Person
class Employee(Person):
    def __init__(self, idNum, fullName, gender, salary):
        super().__init__(idNum,fullName, gender)
        self.salary = salary

    def getEmployee(self):
        return f"{self.idNum} | {self.fullName} | {self.gender} | {self.salary}"

emp = Employee("123123123", "Joem", "male", "900")
person = Person("1233332231", "Joem2", "maleee")

print(emp.getEmployee())
print(person.getPerson())
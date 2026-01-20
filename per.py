class Person:
    def __init__(self, idNum, fullName, gender):
        self.idNum = idNum
        self.fullName = fullName
        self.gender = gender

    def getPerson(self):
        return f"{self.idNum} | {self.fullName} | {self.gender}"
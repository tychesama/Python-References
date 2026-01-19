# dictionary
students = {'Jo': 74,
            'JoJo': 79,
            'Joe': 93}

student_count = len(students)

print(f"JoJo had a grade of {students['JoJo']}.")

print(f"We have {student_count} students!")

del students['JoJo']
print(students)

students['JoJoe'] = {99,98}
print(students)

for student in students.values():
    print(student)

for student,grades in students.items():
    print(f"{student} got {grades}.")


# tuples
a, b = min(99,25,40), max([20,634,410])

print(a)
print(b)


# set
new_set = set()
sl = [2,3,4,2,1,2,3,4,8,5,9,3,2,6,4]

for i in sl:
    new_set.add(i)

print(new_set)

# intersect
# union
# difference

a = input("year: ")

b = int(a) % 4

if (b == 0):
    print(f"{a} is a leap year!")
else:
    print(f"{a} is not a leap year!")

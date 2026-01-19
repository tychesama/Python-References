fin = open("output.txt","r")

file_container = fin.readline()

for char in str(file_container):
    if char.isalpha():
        print(char, end='')
    
fin.close()

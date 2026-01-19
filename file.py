fin = open("words.txt","r")
# readline or readlines
file_container = fin.readlines()


fc = []
for line in file_container:
    fc.append(line.strip())

# fc = [line.strip for line in file_container]

print(fc)
fin.close()

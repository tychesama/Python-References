with open('output.txt', 'w') as fout:
    fout.write('Helllooo')
    fout.write('Helllooo')

# overwrites existing text
with open('output2.txt', 'w') as fslide:
    fslide.write('cringeeee')

# does not overwrite existing text
with open('output3.txt', 'a') as fslide:
    fslide.write('cringeeee')

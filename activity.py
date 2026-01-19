word = input()
vowels = "aeiou"
vow_cnt = 0
baul = []

for char in word:
    if char.lower() in vowels:
        if char.lower() not in baul:
            baul.append(char.lower())
vow_cnt = len(baul)

print(f"You entered the string '{word}' which contains {vow_cnt} vowels.")

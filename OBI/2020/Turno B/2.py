word = str(input())
every_letter = []

for letter in word:
    every_letter.append(letter)

test = str(input())
anagram = True

for i in range(len(test)):
    if (test[i] == "*"):
        continue
    elif (test[i] not in every_letter):
        anagram = False
    elif (test[i] in every_letter):
        every_letter.remove(test[i])

if not anagram: print("N")
else: print("S")

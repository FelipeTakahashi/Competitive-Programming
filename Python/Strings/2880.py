coded = str(input())
crib = str(input())
possible = 0

for temp in range(len(coded) - len(crib) + 1):

    igualdade = True
    test = coded[temp:len(crib)+temp]

    for char in range(len(crib)):
            if test[char] == crib[char]:
                igualdade = False
                break

    if igualdade:
        possible += 1

print(possible)

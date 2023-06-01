first = int(input())
second = int(input())
find = int(input())
number = 0

for i in range(first, second+1):
    total = 0
    for digit in str(i):
        total += int(digit)
        if total > find:
            break
    if (total == find):
        number = i

if (find != 0 and number == 0):
    number = -1

print(number)

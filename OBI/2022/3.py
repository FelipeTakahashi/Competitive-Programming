missing_sum = 0
standard_sum = 0

for i in range(int(input())):
    row = [int(a) for a in input().split()]
    if 0 in row:
        missing_sum = sum(row)
        pos_row = i+1
        pos_col = row.index(0) + 1
    if 0 not in row:
        standard_sum = sum(row)

print(standard_sum-missing_sum)
print(pos_row)
print(pos_col)

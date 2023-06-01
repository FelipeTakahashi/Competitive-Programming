diaria = int(input())
aumento = int(input())
dias = int(input())

if (dias == 1):
    ans = 31 * diaria
elif (dias >= 15):
    ans = (32 - dias) * (diaria + 14 * aumento)

elif (dias < 15):
    ans = (32 - dias) * (diaria + (dias-1) * aumento)

print(ans)

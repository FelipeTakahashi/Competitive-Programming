t, p = map(int, input().split())
d = {}
for i in range(t): # Carro vencedor é i + 1
    a = [int(x) for x in input().split()]
    d[i + 1] = sum(a)

d = sorted(d.items(), key=lambda x: x[1])

for i in range(3):
    print(d.pop(0)[0])

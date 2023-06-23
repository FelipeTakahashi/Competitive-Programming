n = int(input())
lista = [int(a) for a in input().split()]
d = {}
conjunto = set(lista)

for i in set(lista):
    d[i] = 0

for i in lista:
    d[i] += 1

b = []
for k, v in d.items():
    if (v == max(d.values())):
        b.append(k)

print(max(b))

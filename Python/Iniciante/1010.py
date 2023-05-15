p1 = input().split(" ")

p2 = input().split(" ")

id1, u1, v1 = p1

id2, u2, v2 = p2

total = (int(u1) * float(v1)) + (int(u2) * float(v2))

print(f'VALOR A PAGAR: R$ {total:.2f}')

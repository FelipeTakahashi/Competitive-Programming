v = int(input())
p = int(input())

if (v % p == 0):
    for i in range(p):
        print(v//p)

else:
    a = v % p # Quantidade de restos maiores, quantidade de restos normais
    b = int(v/p)
    for i in range(a): # Restos maiores
        print(b + 1)

    for i in range(p-a): # Normais - quantidade de maiores
        print(v//p)

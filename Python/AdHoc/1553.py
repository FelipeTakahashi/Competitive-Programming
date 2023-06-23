while True:
    n, f = map(int, input().split())
    if (n == 0 and f == 0): break

    lista = [int(a) for a in input().split()]
    
    conjunto = set(lista)
    
    d = {}
    for i in conjunto:
        d[i] = 0
        
    for i in lista:
        d[i] += 1
        
    count = 0
    for k, v in d.items():
        if (v >= f):
            count += 1
    print(count)

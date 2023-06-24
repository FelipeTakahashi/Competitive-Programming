m, n = map(int, input().split())
d, everyone = {}, []

names = set()
for i in range(n):
    person, relation, target = map(str, input().split())
    names.update([person, target])
    everyone.extend(([[person, target]]))
    d[person], d[target] = 0, 0

check = {a:a for a in names}

def find(u):
    if check[u] != u: # Se no dicionário de relações, o valor de check[u] não for u, então u não é o pai de si mesmo
        check[u] = find(check[u]) # Agora, check[u] é o pai de u
    return check[u]

def union(u, v):
    u = find(u) # Busca pelo pai de u
    v = find(v) # Busca pelo vai de v
    
    if (u == v): 
        return # Se u e v tiverem o mesmo pai, não há necessidade de unir

    if (d[u] < d[v]): check[u] = v # Quem tiver o maior peso vira o pai
    elif (d[v] < d[u]): check[v] = u # Quem tiver o menor peso vira o pai 
    else: # Se forem iguais, tanto faz quem é atribuído como pai
        check[u] = v
        d[v] += 1

for i in range(len(everyone)):
    union(everyone[i][0], everyone[i][1])

print(len(set([find(i) for i in names])))

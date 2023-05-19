todos, n = map(int, input().split())
d, e, f = todos, todos, todos

for i in range(n):
    rodada = [str(a) for a in input().split()]
    
    if rodada[0] == "C":
        if rodada[1] == "D":
            d -= int(rodada[2])
        elif rodada[1] == "E":
            e -= int(rodada[2])
        elif rodada[1] == "F":
            f -= int(rodada[2])

    if rodada[0] == "V":
        if rodada[1] == "D":
            d += int(rodada[2])
        elif rodada[1] == "E":
            e += int(rodada[2])
        elif rodada[1] == "F":
            f += int(rodada[2])

    if rodada[0] == "A":
        if rodada[1] == "D" and rodada[2] == "F" :
            d += int(rodada[3])
            f -= int(rodada[3])
        if rodada[1] == "D" and rodada[2] == "E" :
            d += int(rodada[3])
            e -= int(rodada[3])
        if rodada[1] == "F" and rodada[2] == "D" :
            f += int(rodada[3])
            d -= int(rodada[3])
        if rodada[1] == "F" and rodada[2] == "E" :
            f += int(rodada[3])
            e -= int(rodada[3])
        if rodada[1] == "E" and rodada[2] == "F" :
            e += int(rodada[3])
            f -= int(rodada[3])
        if rodada[1] == "E" and rodada[2] == "D" :
            e += int(rodada[3])
            d -= int(rodada[3])
print(d, e, f)

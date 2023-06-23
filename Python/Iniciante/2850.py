mov =   {
        "esquerda" : "ingles",
        "direita" : "frances",
        "nenhuma" : "portugues",
        "as duas" : "caiu"
        }
        
movimentos = []
while True:
    try:
        a = str(input())
        movimentos.append(a)
    except EOFError:
        break

for m in movimentos:
    print(mov[m])

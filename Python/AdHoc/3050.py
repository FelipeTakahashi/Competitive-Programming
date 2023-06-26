'''
Diâmetro de uma Árvore Binaria
É o número de nós no caminho mais longo entre dois nós quaisquer da árvore.
Dado por: diametro = altura(subarvore esquerda) + altura(subarvore direita) + 1,
no caso em questão, é necessário considerar a posição do prédio.
'''

def encontraMaior(n, arvore):
    distanciaAuxiliar, predioMaior = -1, n-1
    for i in range(n):
        distanciaAtual = arvore[0] + arvore[i] + i
        if (distanciaAuxiliar < distanciaAtual):
            distanciaAuxiliar = distanciaAtual
            predioMaior = i
    return predioMaior

# Encontrar o prédio maior e depois encontrar a maior distância que existe do maior prédio.

def main():
    n, arvore = int(input()), [int(a) for a in input().split()]
    distanciaMaxima, maiorPredio, distanciaAuxiliar = -1, encontraMaior(n, arvore), -1
    for i in range(n):
        if (i != maiorPredio):
            distanciaAuxiliar = arvore[i] + abs(maiorPredio-i) + arvore[maiorPredio]
            if distanciaAuxiliar > distanciaMaxima:
                distanciaMaxima = distanciaAuxiliar
    print(distanciaMaxima)

main()    

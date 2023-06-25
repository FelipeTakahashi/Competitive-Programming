'''
Algoritmo de Kadane - Programação Dinâmica

Dado um vetor de tamanho N, encontre a maior soma de subvetores contíguos.

    A solução intuitiva é calcular TODAS as somas possíveis e escolher a maior. Porém,
a complexidade do algoritmo é O(N^2). Logo, não é uma solução viável para vetores maiores.

    A solução por meio do Algoritmo de Kadane possui complexidade de tempo O(N). A ideia é 
computar a soma das posições dos subvetores e descobrir a maior soma local. Logo, a maior soma
global será o máximo entre a maior soma local e a maior soma global anterior.

[1, -2, 3, 4] -> 4+3 = 7; 4+(3-2) = 5; 4+(3-2+1) = 6; Máximo Local = 7
[1, -2, 3] - > 3-2 = 1; 3+(-2+1) = 2; Máximo local = 2
[1, -2] -> -2+1 = -1; Máximo local = -1
[1] -> 1; Máximo local = 1
'''

def maxSubArray(vetor, n):
    maximoAtual, maximoAqui = vetor[0], 0

    for i in range(n):
        maximoAqui += vetor[i]
        if (maximoAtual < maximoAqui):
            maximoAtual = maximoAqui

        if (maximoAqui < 0):
            maximoAqui = 0
    return maximoAtual

def main():
    n = int(input())
    valores = [int(a) for a in input().split()]
    print(maxSubArray(valores, n))

main()

def hash(string):
    soma = 0
    index = 0
    for char in string:
        soma += ord(char) - 65 + index
        index += 1
    return soma


for _ in range(int(input())):
    elemento, aux, soma = int(input()), 0, 0
    for _ in range(elemento):
        string = input()
        soma += hash(string) + aux*len(string)
        aux += 1
    print(soma)

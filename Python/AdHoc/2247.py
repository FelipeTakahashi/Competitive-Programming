teste = 0
while True:
    n = int(input())
    if n == 0:
        exit()
    joao = 0
    ze = 0
    teste += 1
    print(f"Teste {teste}")
    for i in range(n):
        valor1, valor2 = map(int, input().split())

        joao += valor1
        ze += valor2

        print(f"{joao - ze}")
    print("")

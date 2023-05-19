for _ in range(int(input())):
    x, y = map(int,input().split())
    
    rafael = (3*x)**2 + y**2

    beto = 2*(x**2) + (5*y)**2

    carlos = -100*x + y**3

    maior = max(rafael,beto,carlos)

    if maior == rafael:
        print("Rafael ganhou")

    elif maior == carlos:
        print("Carlos ganhou")

    else:
        print("Beto ganhou")

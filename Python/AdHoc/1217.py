n = int(input())
dia = 1
somakg, somadin = 0, 0

for i in range(n):
    valor = float(input())
    frutas = [str(a) for a in input().split()]
      
    print(f"day {dia}: {len(frutas)} kg")
    
    dia += 1
    somakg += len(frutas)
    somadin += valor
print(f"{somakg/n:.2f} kg by day")
print(f"R$ {somadin/n:.2f} by day")

t = 1
while True:
    n = int(input())
    if (n == 0):
        break
    
    d = {}
    for i in range(n):
        student, score = map(int, input().split())
        d[student] = score
    
    w = []
    for k, v in d.items():
        if (v == max(d.values())):
            w.append(k)
    m = " ".join(map(str, w))
    
    print(f"Turma {t}")
    print(f"{m} ")
    print()
    t += 1

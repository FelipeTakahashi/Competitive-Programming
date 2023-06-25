t, s = map(int, input().split())
stones = [0] * t

for i in range(s):
    start, heap = map(int, input().split())
    start -= 1
    aux = start

    while (start < t):
        stones[start] = 1
        start += heap

    while (aux >= 0):
        stones[aux] = 1
        aux -= heap
 
for i in range(t):
    print(f"{stones[i]}")

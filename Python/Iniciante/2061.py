tabs, actions = map(int, input().split())

for _ in range(actions):
    action = str(input())
    if action == "fechou":
        tabs += 1
    else:
        tabs -= 1
        
print(tabs)

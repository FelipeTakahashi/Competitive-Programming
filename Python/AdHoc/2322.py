n = int(input())
possui = [int(a) for a in input().split()]

todos = []
for i in range(1, n+1):
    todos.append(i)
    if todos[i-1] not in possui:
        print(todos[i-1])
        break

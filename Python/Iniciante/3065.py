teste = 0
while True:
    n = int(input())
    if n == 0:
        break
    
    teste += 1

    operation = str(input())

    operation = operation.replace("+", " + ")
    operation = operation.replace("-", " - ")

    operation = operation.split()

    if len(operation) == 1:
        total_sum = operation[0]

    else:
        for i in range(1):
            if operation[1] == "+":
                total_sum = int(operation[0]) + int(operation[2])
            elif operation[1] == "-":
                total_sum = int(operation[0]) - int(operation[2])

        for i in range(2, len(operation)-1):
            if operation[i] == "+":
                total_sum += int(operation[i+1])
            elif operation[i] == "-":
                total_sum -= int(operation[i+1])

    print(f"Teste {teste}\n{total_sum}\n")

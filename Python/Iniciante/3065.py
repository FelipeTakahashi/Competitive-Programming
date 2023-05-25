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
        print(f"Teste {teste}\n{total_sum}\n")

    elif len(operation) == 2:
        total_sum = operation[0] + operation[1]
        print(f"Teste {teste}\n{total_sum}\n")

    else:
        for i in range(1):
            if operation[1] == "+":
                total_sum = int(operation[0]) + int(operation[2])
                negative = False
            elif operation[1] == "-":
                total_sum = int(operation[0]) - int(operation[2])
                negative = False

            elif operation[0] == "-" and operation[2] == "+":
                total_sum = (int(operation[1]) * -1) + int(operation[3])
                negative = True
            elif operation[0] == "-"and operation[2] == "-":
                total_sum = (int(operation[1]) * -1) - int(operation[3])
                negative = True

        if not negative:
            for i in range(2, len(operation)-1):
                if operation[i] == "+":
                    total_sum += int(operation[i+1])
                elif operation[i] == "-":
                    total_sum -= int(operation[i+1])

        if negative:
            for i in range(3, len(operation)-1):
                if operation[i] == "+":
                    total_sum += int(operation[i+1])
                elif operation[i] == "-":
                    total_sum -= int(operation[i+1])

        print(f"Teste {teste}\n{total_sum}\n")

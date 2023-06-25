def Check(vector):
    can, minimum = True, min(vector)
    for i in range(len(vector)-1):
        if (abs(vector[i+1] - vector[i]) > 8 or minimum > 8):
            can = False
            break
    return can

def main():
    n = int(input())
    vector = [int(x) for x in input().split()]
    print("S" if Check(sorted(vector)) else "N")

main()

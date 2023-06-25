def escadinha(vector):
    i, counter, limit = 0, 0, len(vector)-1
    while (i < limit):
        try:
            dif = vector[i] - vector[i+1]
    
            while (dif == vector[i] - vector[i+1]):
                i += 1
                if (i == limit): break
            
            counter += 1
        except:
            return counter
            
    return counter

def main():
    n = int(input()) 
    values = [int(a) for a in input().split()]
    if (n == 1): print(1)
    else: print(escadinha(values))

main()

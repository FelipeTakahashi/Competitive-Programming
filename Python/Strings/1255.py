for _ in range(int(input())):
    d = {c : 0 for c in 'abcdefghijklmnopqrstuvwxyz'}
    f = str(input()).lower()
    for letter in f:
        if letter in d:
            d[letter] += 1
        
    for k, v in d.items():
        if (v == max(d.values())):
            print(k, end='')

    print()

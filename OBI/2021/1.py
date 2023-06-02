games = []
for i in range(6):
    played = str(input())
    if (played == "V"):
        games.append(played)

ganhos = len(games)

if 1 <= ganhos <= 2:
    print(3)

elif 3 <= ganhos <= 4:
    print(2)

elif 5 <= ganhos <= 6:
    print(1)

else: print(-1)

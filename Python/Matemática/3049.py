b = int(input())
t = int(input())

area_trapezio = (b+t) * 35
area_nota = 11200 - area_trapezio

if area_trapezio > area_nota:
    print("1")

elif area_nota > area_trapezio:
    print("2")
    
else:
    print("0")

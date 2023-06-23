a = [int(a) for a in input().split()]
fhalf = a[:8]
shalf = a[8:]

if (9 in fhalf and 1 in shalf) or (9 in shalf and 1 in fhalf):
    print('final')
    exit()

elif (9 in fhalf):
    fhalf, shalf = fhalf[:4], fhalf[4:] 

else:
    fhalf, shalf = shalf[:4], shalf[4:]
    
if (9 in fhalf[:2] and 1 in fhalf[:2]) or (9 in fhalf[2:4] and 1 in fhalf[2:4]) or (9 in shalf[:2] and 1 in shalf[:2]) or (9 in shalf[2:4] and 1 in shalf[2:4]):
   print('oitavas')

elif (9 in fhalf[:4] and 1 in fhalf[:4]) or (9 in shalf[:4] and 1 in shalf[:4]):
    print('quartas')

else:
    print('semifinal')

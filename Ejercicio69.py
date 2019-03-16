contadorpar=0
contador5=0
contador=0
while contador5<=80 or contadorpar<100:
    num=int(input("Introduce un número mayor a 0: "))
    contador=contador+1
    if num%2==0:
        contadorpar=contadorpar+1
    if num==5:
        contador5=contador5+1
    if num<0:
        break

print("la cantidad de valores leidos es: ",contador)
print("hay",contadorpar," números pares")
print("hay", contador5," números 5")
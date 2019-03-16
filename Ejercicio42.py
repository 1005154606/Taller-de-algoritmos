num=int(input("Introduce un número menor o igual a 100000: "))
if num>=0 and num<10:
    print("El número tiene una cifras")

if num>=10 and num<100:
    print("El número tiene dos cifras")

if num>=100 and num<1000:
    print("El número tiene tres cifras")

if num>=1000 and num<10000:
    print("El número tiene cuatro cifras")

if num>=10000 and num<100000:
    print("El número tiene cinco cifras")

if num==100000:
    print("El número tiene seis cifras")

if num>100000 or num<0:
    print("El número ingresado no es valido")
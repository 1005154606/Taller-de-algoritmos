num=int(input("Introduce un número:"))
if num==0:
    print("El 0 no cumple ninguna condición")
else:
    if num%2==0:
        if num>0:
            print("El número es par positivo")

        else:
            print("El número es par negativo")
    else:
        if num>0:
            print("El número es impar positivo")
        else:
            print("El número es impar negativo")

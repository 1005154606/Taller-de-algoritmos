num1=float(input("Introduce el primer número: "))
num2=float(input("Introduce el segundo número: "))
num3=float(input("Introduce el tercer número: "))

primero=num1+num2
if primero==num3:
    print("La suma de", num1," y ",num2," es igual que", num3)
else:
    if primero>num3:
        print("La suma de ",num1," y ",num2, "es mayor que ",num3)

    else:
        print("La suma de ",num1," y ",num2, "es menor que que ",num3)
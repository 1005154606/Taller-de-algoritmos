num1=float(input("introduce el priemr número: "))
num2=float(input("introduce el segundo múmero: "))
num3=float(input("Introduce el tercer número: "))

if num1>num2 and num2>num3:
    print(num1," Es el mayor")
else:
    if num3>num2 and num2>num1:
        print(num3," es el mayor")
    else:
        print(num2," es el mayor")

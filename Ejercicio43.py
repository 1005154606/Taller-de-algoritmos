num1=float(input("Introduce el primer número: "))
num2=float(input("Introduce el segundo número: "))
num3=float(input("Introduce el tercer número: "))
if num1>num2 and num2>num3:
    print("El número está disminuyendo")
elif num3>num2 and num2>num1:
    print("el número está incrementando ")
else:
    print("Ni se incrementa ni se disminuye")

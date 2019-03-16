num1=float(input("Introduce el primer número: "))
num2=float(input("Introduce el segundo número: "))
num3=float(input("Introduce el tercer número: "))
if num1==num2 and num2==num3:
    print(num1, num2, num3, "son iguales")

elif num1==num2:
    print(num1,"es igual a", num2)
elif num1==num3:
    print(num1,"es igual a", num3)
elif num3==num2:
    print(num3," es igual a", num2)
elif num1==num2 and num2==num3:
    print(num1, num2, num3, "son iguales")
else:
    print("Ningún número es igual")

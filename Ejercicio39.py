a=float(input("Introduce el valor de a: "))
b=float(input("Introduce el valor de b: "))
c=float(input("Introduce el valor de c: "))
d=b**2-4*a*c
if d<0:
    print("La ecuación no tiene solución")
else:
    if a==0:
        print("Print el valor de a no puede ser 0")
    else:
        import math
        x=b*-1
        raiz=math.sqrt(d)
        positivo=(x+raiz)/2*a
        negativo=(x-raiz)/2*a
        print("las soluciones son", positivo," y", negativo)
        print(x)
        print(d)
        print(raiz)
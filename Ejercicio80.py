a=0
n=int(input("ingresar numeros de flias: "))
for i in range(n+1):
    for l in range(0,i):
        z=i+l
        print(end=str(z))
    print(" ")
    i=i+a
    a=a+1
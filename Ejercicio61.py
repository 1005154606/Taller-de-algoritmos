n=int(input("Introduce un número: "))
m=int(input("Introduce un número: "))
if m>n:
    for x in range(n, m+1):
        print(x)
else:
    print("M tiene que ser mayor que n")

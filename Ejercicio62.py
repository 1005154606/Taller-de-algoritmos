n=int(input("Introduce un número: "))
m=int(input("Introduce un número: "))
c=0
if m>n:
    for x in range(n, m+1):

        c=c+x


else:
    print("M tiene que ser mayor que n")
print(c)


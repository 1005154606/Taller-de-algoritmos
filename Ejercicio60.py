n=int(input("Introduce un número: "))
for x in range(1, n):
    if x%2!=0:
        print(x)
    b=x%2
    if b==0:
        c=x*-1
        print(c)
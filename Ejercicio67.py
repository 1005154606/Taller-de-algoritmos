c1=0
c2=0
c3=0
n=int(input("Introduce un número: "))
for x in range(0, n):
    if x==100:
        c3=c3+1
    if x>100:
        c1=c1+1
    if x<100:
        c2=c2+1
print("Hubieron", c1," números mayores a cien")
print("Hubieron", c2," números menores a cien")
print("Hubieron", c3," números iguales a cien")
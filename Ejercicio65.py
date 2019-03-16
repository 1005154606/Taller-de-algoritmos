cp=0
ci=0
n=int(input("Introduce un número: "))
for x in range(0,n):
    if x %2==0:
        cp=cp+1
    else:
        ci=ci+1
promp=cp/n
promi=ci/n
print("El promedio de los pares es", promp)
print("El promedio de los impares es", promi)
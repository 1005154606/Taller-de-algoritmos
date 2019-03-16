cpos=0
cne=0
cpar=0
cimpar=0
cmul=0
y=int(input("Introduce un número: "))
n=int(input("Introduce un número: "))
for x in range(y, n+1):
    if x%2==0:
        cpar=cpar+1
    else:
        cimpar=cimpar+1
    if x>0:
        cpos=cpos+1
    else:
        cne=cne+1
    if x%8==0:
        cmul=cmul+1
print("hay",cpos," números positivos")
print("hay",cne," números negativos")
print("hay",cpar," números pares")
print("hay",cimpar," números impares")
print("hay",cmul," números multiplos de ocho")
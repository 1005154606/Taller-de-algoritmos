b=int(input("Introduce el la cantidad de dinero deseada: "))
b50=int(b/50000)
r50=b%50000
b20=int(r50/20000)
r20=r50%20000
b10=int(r20/10000)
r10=r20%10000
b5=int(r10/5000)
r5=r10%5000
b2=int(r5/5000)
r2=r5%5000
b1=int(r2/1000)
print("son",b50,"billetes de 50000, ",b20,"billetes de 20000, ",b10,"billetes de 10000,",b5, "billetes de 5000", b2,"billetes de 2000",b1,"de 1000")